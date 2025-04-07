from dataclasses import dataclass, field
from table.piece_enum import PieceEnum
from typing import Dict, Final


PIECE_DEFAULT_REPRESENTATION: Final[Dict[PieceEnum, str]] = {
    PieceEnum.PAWN: "P",
    PieceEnum.ROOK: "R",
    PieceEnum.KNIGHT: "N",
    PieceEnum.BISHOP: "B",
    PieceEnum.QUEEN: "Q",
    PieceEnum.KING: "K",

    PieceEnum.EMPTY: " "
}

@dataclass
class Representations:
    white: Dict[PieceEnum, str] = field(default_factory = PIECE_DEFAULT_REPRESENTATION.copy)
    black: Dict[PieceEnum, str] = field(default_factory = PIECE_DEFAULT_REPRESENTATION.copy)

@dataclass
class Config:
    representations: Representations = field(default_factory = Representations)
