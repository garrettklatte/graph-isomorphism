import dataclasses
import json

from definitions.context import Context
from gateways.graph_gateway import GraphGateway
from use_cases import retrieve_graph


def lambda_handler(event, context):

    http_method = event["httpMethod"]
    difficulty = event["pathParameters"]["difficulty"]
    uri = int(event["pathParameters"]["uri"])
    status_code = 200

    context = Context(GraphGateway())

    if http_method == "GET":
        graph = retrieve_graph(context, difficulty, uri)
        return {
            "statusCode": status_code,
            "body": json.dumps(dataclasses.asdict(graph)),
            "headers": {"Access-Control-Allow-Origin": "*"},
        }
