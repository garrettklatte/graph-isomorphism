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
    "vertices": ["A", "B", "C", "D", "E"],
    "source": {
        "A": {"x": 50, "y": 10},
        "B": {"x": 75, "y": 90},
        "C": {"x": 10, "y": 40},
        "D": {"x": 90, "y": 40},
        "E": {"x": 25, "y": 90},
    },
    "target": {
        "A": {"x": 50, "y": 10},
        "B": {"x": 90, "y": 40},
        "C": {"x": 75, "y": 90},
        "D": {"x": 25, "y": 90},
        "E": {"x": 10, "y": 40},
    },
    "edges": [
        {"start": "A", "end": "B"},
        {"start": "B", "end": "C"},
        {"start": "C", "end": "D"},
        {"start": "D", "end": "E"},
        {"start": "E", "end": "A"},
    ],
}

hard_graph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "source": {
        "A": {"x": 30, "y": 10},
        "G": {"x": 30, "y": 36.7},
        "F": {"x": 30, "y": 63.3},
        "D": {"x": 30, "y": 90},
        "H": {"x": 70, "y": 10},
        "B": {"x": 70, "y": 36.7},
        "C": {"x": 70, "y": 63.3},
        "E": {"x": 70, "y": 90},
    },
    "target": {
        "A": {"x": 10, "y": 10},
        "B": {"x": 90, "y": 10},
        "C": {"x": 10, "y": 90},
        "D": {"x": 90, "y": 90},
        "E": {"x": 30, "y": 30},
        "F": {"x": 70, "y": 30},
        "G": {"x": 30, "y": 70},
        "H": {"x": 70, "y": 70},
    },
    "edges": [
        {"start": "A", "end": "B"},
        {"start": "A", "end": "C"},
        {"start": "A", "end": "E"},
        {"start": "G", "end": "H"},
        {"start": "G", "end": "C"},
        {"start": "G", "end": "E"},
        {"start": "F", "end": "H"},
        {"start": "F", "end": "B"},
        {"start": "F", "end": "E"},
        {"start": "D", "end": "H"},
        {"start": "D", "end": "B"},
        {"start": "D", "end": "C"},
    ],
}


def lambda_handler(event, context):

    http_method = event["httpMethod"]
    difficulty = event["pathParameters"]["difficulty"]
    uri = event["pathParameters"]["uri"]
    status_code = 200

    if difficulty == "easy":
        body = easy_graph
    elif difficulty == "medium":
        body = medium_graph
    else:
        body = hard_graph

    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
