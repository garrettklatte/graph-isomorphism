"""Module defining the Context class."""
# pylint: disable=too-few-public-methods
import dataclasses

from gateways.graph_gateway import GraphGateway


@dataclasses.dataclass
class Context:
    """Class holding the context for the use cases."""

    graph_gateway: GraphGateway
