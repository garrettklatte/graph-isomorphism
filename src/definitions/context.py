import dataclasses

from gateways.graph_gateway import GraphGateway


@dataclasses.dataclass
class Context:
    graph_gateway: GraphGateway
