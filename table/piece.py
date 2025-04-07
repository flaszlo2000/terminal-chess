from dataclasses import dataclass, field
from table.piece_enum import PieceEnum
from globals import CONFIG


@dataclass
class Piece:
    _type: PieceEnum
    white: bool = field(kw_only = True)

    representation: str = field(default = "")

    
    def _get_piece_representation(self) -> str:
        return CONFIG.representations.white[self._type] if self.white else CONFIG.representations.black[self._type]

    def __post_init__(self) -> None:
        assert self._type is not None

        if len(self.representation) == 0:
            self.representation = self._get_piece_representation()
