from typing import Any, Dict

import boto3

from definitions.graph import Graph


class GraphGateway:
    @staticmethod
    def fetch_graph(difficulty: str, identifier: int) -> Graph:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("Graphs")

        request = GraphGateway._make_request(difficulty, identifier)

        response = table.get_item(**request)

        return GraphGateway._pluck_graph(response)

    @staticmethod
    def _make_request(difficulty: str, identifier: int) -> Dict[str, Dict[str, Any]]:
        if not difficulty.lower() in ("easy", "medium", "hard"):
            raise ValueError

        return {"Key": {"Difficulty": difficulty.upper(), "Id": identifier}}

    @staticmethod
    def _pluck_graph(response: Dict[str, Any]) -> Graph:
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
        vertices = [vertex for vertex in source]

        return Graph(edges, source, target, vertices)
