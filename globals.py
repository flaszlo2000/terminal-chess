from typing import Final, List, Dict
from config import Config
from table.piece_enum import PieceEnum


ALLOWED_SQUARE_HEIGHTS: Final[List[int]] = [1, 3, 5, 7] # TODO: read this from env?


PIECE_MAP: Final[Dict[str, PieceEnum]] = {
    "P": PieceEnum.PAWN,
    "R": PieceEnum.ROOK,
    "N": PieceEnum.KNIGHT,
    "B": PieceEnum.BISHOP,
    "Q": PieceEnum.QUEEN,
    "K": PieceEnum.KING
}

# TODO: add option to change this to unicode characters
CONFIG: Final[Config] = Config() 