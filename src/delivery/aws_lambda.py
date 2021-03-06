"""Module defining the lambda delivery."""
# pylint: disable=wrong-import-position,too-many-return-statements
import dataclasses
import decimal
import json
import os
from typing import Any, Dict, Optional
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from definitions.context import Context
from definitions.exception import InvalidDifficulty, GraphNotFound
from gateways.graph_gateway import GraphGateway
from use_cases import retrieve_graph, retrieve_graphs


class DecimalEncoder(json.JSONEncoder):
    """Class for encoding Dnecimal objects in JSON."""

    # pylint: disable=arguments-differ,method-hidden
    def default(self, obj: Any) -> Any:
        """Extend the default JSON encoder to handle Decimal objects."""
        if isinstance(obj, decimal.Decimal):
            if abs(obj) % 1 > 0:
                return float(obj)
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def http_response(status_code: int, message: Any) -> Dict[str, Any]:
    """Generate an http response with 'status_code' with 'message' in the body."""
    return {
        "statusCode": status_code,
        "body": json.dumps(message, cls=DecimalEncoder),
        "headers": {"Access-Control-Allow-Origin": "*"},
    }


def lambda_handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    """Method that handles an 'event' with 'context'."""
    http_method = event["httpMethod"]
    try:
        difficulty = event["pathParameters"]["difficulty"]
    except KeyError:
        difficulty = None
    try:
        uri: Optional[int] = int(event["pathParameters"]["uri"])
    except KeyError:
        uri = None

    context = Context(GraphGateway())

    if http_method == "GET":
        if difficulty and uri:
            try:
                graph = retrieve_graph(context, difficulty, uri)
            except InvalidDifficulty:
                return http_response(400, f"Unrecognized difficulty: {difficulty}")
            except GraphNotFound:
                return http_response(
                    404,
                    f"Unrecognized resource: difficulty {difficulty} with uri {uri}",
                )
            return http_response(200, dataclasses.asdict(graph))
        if difficulty and not uri:
            try:
                graphs = retrieve_graphs(context, difficulty)
            except InvalidDifficulty:
                return http_response(400, f"Unrecognized difficulty: {difficulty}")
            return http_response(200, graphs)
        return http_response(400, f"{difficulty} must be specified.")
    return http_response(501, f"{http_method} is not implemented.")
