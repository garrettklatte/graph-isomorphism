"""Module defining all exceptions that can be raised by a use case."""


class GraphNotFound(Exception):
    """Exception to be raised when the requested graph cannot be found."""


class InvalidDifficulty(Exception):
    """Exception to be raised when the user specifies an invalid difficulty."""
