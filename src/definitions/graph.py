import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class Graph:
    edges: List[Dict[str, str]]
    source: Dict[str, Dict[str, int]]
    target: Dict[str, Dict[str, int]]
    vertices: List[str]
