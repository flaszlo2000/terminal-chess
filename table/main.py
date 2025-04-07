from table.table import Table
from typing import Final
from globals import PIECE_MAP
from table.piece import Piece

_MINOR_PIECES_IN_ORDER: Final[str] = "RNBQKBNR"

def crate_table() -> Table:
    white = [Piece(PIECE_MAP[piece_sign], white = True) for piece_sign in "P" * 8 + _MINOR_PIECES_IN_ORDER]
    black = [Piece(PIECE_MAP[piece_sign], white = False) for piece_sign in _MINOR_PIECES_IN_ORDER + "P" * 8]

    return Table(white, black)
