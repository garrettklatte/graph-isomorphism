import json

easy_graph = {
    "vertices": ["A", "B", "C", "D"],
    "source": {
        "A": {"x": 10, "y": 10},
        "B": {"x": 10, "y": 90},
        "C": {"x": 90, "y": 10},
        "D": {"x": 90, "y": 90},
    },
    "target": {
        "A": {"x": 10, "y": 10},
        "B": {"x": 90, "y": 10},
        "C": {"x": 90, "y": 90},
        "D": {"x": 10, "y": 90},
    },
    "edges": [
        {"start": "A", "end": "B"},
        {"start": "B", "end": "C"},
        {"start": "C", "end": "D"},
        {"start": "D", "end": "A"},
    ],
}

medium_graph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "source": {
        "A": {"x": 10, "y": 10},
        "B": {"x": 10, "y": 90},
        "C": {"x": 90, "y": 10},
        "D": {"x": 90, "y": 90},
        "E": {"x": 30, "y": 30},
        "F": {"x": 70, "y": 30},
        "G": {"x": 30, "y": 70},
        "H": {"x": 70, "y": 70},
    },
    "target": {
        "A": {"x": 30, "y": 10},
        "B": {"x": 30, "y": 36.7},
        "C": {"x": 30, "y": 63.3},
        "D": {"x": 30, "y": 90},
        "E": {"x": 70, "y": 10},
        "F": {"x": 70, "y": 36.7},
        "G": {"x": 70, "y": 63.3},
        "H": {"x": 70, "y": 90},
    },
    "edges": [
        {"start": "A", "end": "B"},
        {"start": "B", "end": "C"},
        {"start": "C", "end": "D"},
        {"start": "D", "end": "A"},
        {"start": "A", "end": "E"},
        {"start": "B", "end": "F"},
        {"start": "C", "end": "G"},
        {"start": "D", "end": "H"},
        {"start": "E", "end": "F"},
        {"start": "F", "end": "H"},
        {"start": "E", "end": "G"},
        {"start": "G", "end": "H"},
    ],
}

hard_graph = {}


def lambda_handler(event, context):

    http_method = event["httpMethod"]
    difficulty = event["pathParameters"]["difficulty"]
    uri = event["pathParameters"]["uri"]
    status_code = 200

    if difficulty == "easy":
        body = {"graph": easy_graph}
    elif difficulty == "medium":
        body = {"graph": medium_graph}
    else:
        body = {"graph": hard_graph}

    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
