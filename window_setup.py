from dataclasses import dataclass, field
from _curses import window as CursesWindow
from globals import ALLOWED_SQUARE_HEIGHTS
from table.table import Table


@dataclass
class WindowSetup:
    window: CursesWindow
    table: Table

    square_height: int = field(default = ALLOWED_SQUARE_HEIGHTS[0])

    def __post_init__(self) -> None:
        assert self.square_height in ALLOWED_SQUARE_HEIGHTS
