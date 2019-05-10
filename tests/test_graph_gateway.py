"""Tests for the graph_gateway module."""
# pylint: disable=protected-access,invalid-name
import pytest

from definitions.exception import InvalidDifficulty, GraphNotFound
from definitions.graph import Graph
from gateways.graph_gateway import GraphGateway


def test_make_easy_request():
    """Return a request for an EASY graph."""
    # Given
    difficulty = "easy"
    identifier = 7

    # When
    request = GraphGateway._make_request(difficulty, identifier)

    # Then
    assert request == {"Key": {"Difficulty": "EASY", "Id": 7}}


def test_make_medium_request():
    """Return a request for a MEDIUM graph."""
    # Given
    difficulty = "medium"
    identifier = 7

    # When
    request = GraphGateway._make_request(difficulty, identifier)

    # Then
    assert request == {"Key": {"Difficulty": "MEDIUM", "Id": 7}}


def test_make_hard_request():
    """Return a request for a HARD graph."""
    # Given
    difficulty = "hard"
    identifier = 7

    # When
    request = GraphGateway._make_request(difficulty, identifier)

    # Then
    assert request == {"Key": {"Difficulty": "HARD", "Id": 7}}


def test_raise_InvalidDifficulty_on_unrecognized_difficulty():
    """Raise an InvalidDifficulty expection when the user specifies an unrecognized difficulty."""
    # Given
    difficulty = "uber"
    identifier = 7

    # When & Then
    with pytest.raises(InvalidDifficulty):
        GraphGateway._make_request(difficulty, identifier)


def test_pluck_graph():
    """Return a graph."""
    # Given
    response = {
        "Item": {
            "Edges": [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]],
            "Source": {"A": [10, 10], "B": [10, 90], "C": [90, 10], "D": [90, 90]},
            "Target": {"A": [10, 10], "B": [10, 90], "C": [90, 90], "D": [90, 10]},
        }
    }

    # When
    graph = GraphGateway._pluck_graph(response)

    # Then
    assert graph == Graph(
        edges=[
            {"start": "A", "end": "B"},
            {"start": "B", "end": "C"},
            {"start": "C", "end": "D"},
            {"start": "D", "end": "A"},
        ],
        source={
            "A": {"x": 10, "y": 10},
            "B": {"x": 10, "y": 90},
            "C": {"x": 90, "y": 10},
            "D": {"x": 90, "y": 90},
        },
        target={
            "A": {"x": 10, "y": 10},
            "B": {"x": 10, "y": 90},
            "C": {"x": 90, "y": 90},
            "D": {"x": 90, "y": 10},
        },
        vertices=["A", "B", "C", "D"],
    )


def test_raise_GraphNotFound_when_graph_is_not_found():
    """Raise a GraphNotFound expection when the response does not contain an item."""
    # Given
    response = {"Item": {}}

    # When & Then
    with pytest.raises(GraphNotFound):
        GraphGateway._pluck_graph(response)
