from dataclasses import dataclass, field
from typing import List, Optional, Dict
from table.piece import Piece
from console_drawing.coord import Coord


@dataclass
class Table:
    white_pieces: List[Piece] # TODO: remove this
    black_pieces: List[Piece] # TODO: remove this

    full_content: Optional[Dict[int, Dict[int, Optional[Piece]]]] = field(default = None)

    def __post_init__(self) -> None:
        assert len(self.white_pieces) == 16
        assert len(self.black_pieces) == 16

        if self.full_content is None:
            self.full_content = {}

            self.full_content[0] = { i:piece for i, piece in enumerate(self.black_pieces[:8])}
            self.full_content[1] = { i:piece for i, piece in enumerate(self.black_pieces[8:])}

            for i in range(2, 6):
                self.full_content[i] = { i:None for i in range(8) }

            self.full_content[6] = { i:piece for i, piece in enumerate(self.white_pieces[:8])}
            self.full_content[7] = { i:piece for i, piece in enumerate(self.white_pieces[8:])}


    def move_piece(self, old_coord: Coord, new_coord: Coord) -> None:
        assert self.full_content is not None

        piece = self.full_content[old_coord.y].pop(old_coord.x)
        self.full_content[old_coord.y][old_coord.x] = None
        assert piece is not None

        self.full_content[new_coord.y][new_coord.x] = piece
