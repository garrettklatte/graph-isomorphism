"""Module defining the Graph class."""
# pylint: disable=too-few-public-methods
import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class Graph:
    """Class representing a Graph.
    'edges' is a list of undirected edges between two vertices.
    'source' is a mapping of vertices to (x, y) source starting positions.
    'target' is a mapping of vertices to (x, y) target starting positions.
    'vertices' is a list of vertices.
    """

    edges: List[Dict[str, str]]
    source: Dict[str, Dict[str, int]]
    target: Dict[str, Dict[str, int]]
    vertices: List[str]
