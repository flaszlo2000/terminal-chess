from dataclasses import dataclass, field
from typing import List, Optional, Dict
from table.piece import Piece


@dataclass
class Table:
    white_pieces: List[Piece]
    black_pieces: List[Piece]

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
