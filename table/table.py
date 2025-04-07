from dataclasses import dataclass, field
from typing import Dict, Self, List, Final, Optional
from table.piece import Piece
from console_drawing.coord import Coord
from globals import PIECE_MAP, MINOR_PIECES_IN_ORDER, PAWNS, PAWN_LINES, MINOR_PIECE_LINES


@dataclass
class PieceWithCoord:
    piece: Piece
    coord: Coord

@dataclass
class Table: # TODO: SEPARATE THIS
    full_content: Dict[int, Dict[int, Piece]] = field(default_factory = dict)
    _selected_piece: Optional[PieceWithCoord] = field(default = None)


    @staticmethod
    def setup_pieces(line: Dict[int, Piece], pieces: str, *, is_white: bool) -> Dict[int, Piece]:
        assert len(pieces) == 8
        
        return { i:Piece(PIECE_MAP[piece_sign], white = is_white) for i, piece_sign in enumerate(pieces)}

    @staticmethod
    def setup_lines_for_both_colors(table: Dict[int, Dict[int, Piece]], piece_lines: List[int], pieces: str) -> None:
        for white, line_index in enumerate(piece_lines):
            table[line_index] = Table.setup_pieces({}, pieces, is_white = bool(white))

    @staticmethod
    def setup_table(empty_table: Dict[int, Dict[int, Piece]]) -> None:
        Table.setup_lines_for_both_colors(empty_table, PAWN_LINES, PAWNS)
        Table.setup_lines_for_both_colors(empty_table, MINOR_PIECE_LINES, MINOR_PIECES_IN_ORDER)

        # NOTE: cannot use setup_lines_for_both_colors because first line would be miscolored
        EMPTY_TABLE_LINES: Final[List[int]] = list(range(2, 6))
        EMPTY_LINE: Final[str] = " " * 8
        for empty_line_index in EMPTY_TABLE_LINES:
            empty_table[empty_line_index] = Table.setup_pieces({}, EMPTY_LINE, is_white = True)

    @classmethod
    def create(cls) -> Self:
        result = cls()
        cls.setup_table(result.full_content)

        return result

    def move_piece(self, old_coord: Coord, new_coord: Coord) -> None:
        assert new_coord.x >= 0 and new_coord.y >= 0
        assert new_coord.x <= 7 and new_coord.y <= 7

        piece: Piece = self.full_content[old_coord.y].pop(old_coord.x)
        assert piece.hasValue()

        self.full_content[old_coord.y][old_coord.x] = self.full_content[new_coord.y][new_coord.x]
        self.full_content[new_coord.y][new_coord.x] = piece

    def getPiece(self, coord: Coord) -> Piece:
        return self.full_content[coord.y][coord.x]

    def hasSelectedPiece(self) -> bool:
        return self._selected_piece is not None

    def removeSelectedPiece(self) -> None:
        assert self._selected_piece is not None

        self._selected_piece.piece.special_color = None
        self._selected_piece = None

    def selectPieceAt(self, coord: Coord) -> None:
        piece_to_select = self.getPiece(coord)
        assert piece_to_select.hasValue()

        if self.hasSelectedPiece(): self.removeSelectedPiece()

        piece_to_select.special_color = 2 # red # TODO: refactor this
        self._selected_piece = PieceWithCoord(piece_to_select, coord)

    def getSelectedPieceCoord(self) -> Coord:
        assert self._selected_piece is not None

        return self._selected_piece.coord