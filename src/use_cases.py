"""Use cases."""
from typing import List

from definitions.context import Context
from definitions.graph import Graph


def retrieve_graph(context: Context, difficulty: str, uri: int) -> Graph:
    """Using 'context', retrieve the graph uniquely identified by 'difficulty' and 'uri'."""
    return context.graph_gateway.fetch_graph(difficulty, uri)


def retrieve_graphs(context: Context, difficulty: str) -> List[int]:
    """Using 'context', retrieve a list of uris for graphs with 'difficulty'."""
    return context.graph_gateway.fetch_uris(difficulty)
