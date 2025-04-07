from window_setup import WindowSetup
from console_drawing.coord import Coord
from typing import Optional, Final
from curses import color_pair as curses_color_pair


def generate_chessboard_coord(window_setup: WindowSetup, coord: Coord, content: str, color: Optional[int] = None) -> None:
    # TODO: add comments!
    assert coord.x >= 0 and coord.y >= 0
    assert len(content) == 1

    start_x = coord.x * (window_setup.square_height * 2 + 2)
    start_y = coord.y * (window_setup.square_height + 1)
    DIVIDER_LINE_FIX_PART: Final[str] = "-" * (window_setup.square_height * 2 + 1)
    
    window_setup.window.move(start_y, start_x)

    # we draw the top-right triangle of the square
    if coord.y == 0 : # we override the first topline
        table_top_line_part = DIVIDER_LINE_FIX_PART + "-"
    else:
        if coord.x != 7:    
            table_top_line_part = DIVIDER_LINE_FIX_PART + "+"
        else:
            table_top_line_part = DIVIDER_LINE_FIX_PART + "|"

    window_setup.window.addstr(table_top_line_part)
    window_setup.window.move(start_y + 1, start_x + (window_setup.square_height * 2 + 1))
    window_setup.window.vline("|", window_setup.square_height)

    # we draw the bottom part of the last line of the board
    if coord.y == 7:
        window_setup.window.move(start_y + window_setup.square_height + 1, start_x)
        window_setup.window.addstr(DIVIDER_LINE_FIX_PART + "-")

    # we put the piece sign into the square 
    center_x = start_x + ((window_setup.square_height * 2 + 1) // 2) 
    center_y = start_y + ((window_setup.square_height ) // 2 + 1)

    window_setup.window.move(center_y, center_x)

    if color is None:
        window_setup.window.addch(content)
    else:
        window_setup.window.addch(content, curses_color_pair(color))

def draw_table(window_setup: WindowSetup) -> None:
    assert window_setup.table.full_content is not None

    for y, line in window_setup.table.full_content.items():
        for x, piece in line.items():
            generate_chessboard_coord(window_setup, Coord(x, y), piece.representation, not piece.white)
