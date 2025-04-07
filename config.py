from dataclasses import dataclass, field
from table.piece_enum import PieceEnum
from typing import Dict


def _get_default_piece_representations() -> Dict[PieceEnum, str]:
    return {
        PieceEnum.PAWN: "P",
        PieceEnum.ROOK: "R",
        PieceEnum.KNIGHT: "N",
        PieceEnum.BISHOP: "B",
        PieceEnum.QUEEN: "Q",
        PieceEnum.KING: "K"
    }

@dataclass
class Representations:
    white: Dict[PieceEnum, str] = field(default_factory = _get_default_piece_representations)
    black: Dict[PieceEnum, str] = field(default_factory = _get_default_piece_representations)

@dataclass
class Config:
    representations: Representations = field(default_factory = Representations)
