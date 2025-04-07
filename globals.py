from typing import Final, List

ALLOWED_SQUARE_HEIGHTS: Final[List[int]] = [1, 3, 5, 7] # TODO: read this from env?

DEFAULT_TABLE: Final[List[str]] = [ # TODO: Add option to change this to unicode pieces!
    "RNBQKBNR",
    "P" * 8,
    *[" " * 8] * 4,
    "P" * 8,
    "RNBQKBNR"
]