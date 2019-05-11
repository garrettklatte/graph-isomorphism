"""Module defining the GraphGateway class."""
# pylint: disable=too-few-public-methods
from typing import Any, Dict, List

import boto3
from boto3.dynamodb.conditions import Key

from definitions.exception import GraphNotFound, InvalidDifficulty
from definitions.graph import Graph


class GraphGateway:
    """Class for interacting with the graph datastore."""

    @staticmethod
    def fetch_graph(difficulty: str, identifier: int) -> Graph:
        """Fetch the graph uniquely identified by 'difficulty' and 'identifier'. If 'difficulty'
        is not a valid difficulty, raise InvalidDifficulty. If no such graph exists, raise
        GraphNotFound. Otherwise, return the graph.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("Graphs")

        request = GraphGateway._make_request(difficulty, identifier)

        response = table.get_item(**request)

        return GraphGateway._pluck_graph(response)

    @staticmethod
    def fetch_uris(difficulty: str) -> List[int]:
        """Fetch a list of uris for graphs with 'difficulty'. If 'difficulty' is not a valid
        difficulty, raise InvalidDifficulty. Otherwise, return the list.
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("Graphs")

        request = GraphGateway._make_uris_request(difficulty)
        response = table.query(**request)
        return GraphGateway._pluck_uris(response)

    @staticmethod
    def _make_uris_request(difficulty: str) -> Dict[str, Any]:
        GraphGateway._validate_difficulty(difficulty)
        return {
            "KeyConditionExpression": Key("Difficulty").eq(difficulty.upper()),
            "ProjectionExpression": "Id",
        }

    @staticmethod
    def _pluck_uris(response: Dict[str, Any]) -> List[int]:
        return [item["Id"] for item in response["Items"]]

    @staticmethod
    def _validate_difficulty(difficulty: str) -> None:
        if not difficulty.lower() in ("easy", "medium", "hard"):
            raise InvalidDifficulty

    @staticmethod
    def _make_request(difficulty: str, identifier: int) -> Dict[str, Dict[str, Any]]:
        GraphGateway._validate_difficulty(difficulty)
        return {"Key": {"Difficulty": difficulty.upper(), "Id": identifier}}

    @staticmethod
    def _pluck_graph(response: Dict[str, Any]) -> Graph:
        try:
            edges = [
                {"start": edge[0], "end": edge[1]} for edge in response["Item"]["Edges"]
            ]
            source = {
                vertex: {"x": coordinates[0], "y": coordinates[1]}
                for vertex, coordinates in response["Item"]["Source"].items()
            }
            target = {
                vertex: {"x": coordinates[0], "y": coordinates[1]}
                for vertex, coordinates in response["Item"]["Target"].items()
            }
        except KeyError:
            raise GraphNotFound

        vertices = [vertex for vertex in source]
        return Graph(edges, source, target, vertices)
