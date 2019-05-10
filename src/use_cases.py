from definitions.context import Context
from definitions.graph import Graph


def retrive_graph(context: Context, difficulty: str, uri: int) -> Graph:
    return context.graph_gateway.fetch_graph(difficulty, uri)
