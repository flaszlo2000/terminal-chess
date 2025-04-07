from window_setup import WindowSetup
from console_drawing.board_helpers import get_board_height, get_board_width
from globals import ALLOWED_SQUARE_HEIGHTS
from console_drawing.main import draw_table
from typing import Tuple


def _update(window_setup: WindowSetup) -> None:
    window_setup.window.clear()
    draw_table(window_setup) #! FIXME: possibly bug if non-default table is used!

def _make_table_smaller(window_setup: WindowSetup) -> None:
    window_setup.square_height = ALLOWED_SQUARE_HEIGHTS[ALLOWED_SQUARE_HEIGHTS.index(window_setup.square_height)-1] #! FIXME: wrong indexing with smallest!

    _update(window_setup)
    
def _make_table_bigger(window_setup: WindowSetup, bigger_board_size: int) -> None:
    window_setup.square_height = bigger_board_size

    _update(window_setup)

def _is_there_a_bigger_board(square_height: int) -> bool:
    return ALLOWED_SQUARE_HEIGHTS[-1] > square_height

def _get_biggest_applicable_board_size(square_height: int, new_size: Tuple[int, int]) -> int:
    result = square_height
    
    for board_size in ALLOWED_SQUARE_HEIGHTS[::-1]:
        if new_size[0] >= get_board_height(board_size) and new_size[1] >= get_board_width(board_size):
            result = board_size
            break
    
    return result

def on_resize(window_setup: WindowSetup) -> None: # TODO: make sure to add option to disable this, at least partially
    new_size = window_setup.window.getmaxyx()
    current_board_size = window_setup.square_height

    if new_size[0] < get_board_height(current_board_size) or new_size[1] < get_board_width(current_board_size):
        _make_table_smaller(window_setup)

    if _is_there_a_bigger_board(current_board_size):
        biggest_applicable_board_size = _get_biggest_applicable_board_size(current_board_size, new_size)

        if biggest_applicable_board_size > current_board_size:
            _make_table_bigger(window_setup, biggest_applicable_board_size)
