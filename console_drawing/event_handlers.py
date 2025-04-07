from window_setup import WindowSetup
from console_drawing.board_helpers import get_board_height, get_board_width
from globals import ALLOWED_SQUARE_HEIGHTS
from console_drawing.main import draw_table


def _update(window_setup: WindowSetup) -> None:
    window_setup.window.clear()
    draw_table(window_setup) #! FIXME: possibly bug if non-default table is used!

def _make_table_smaller(window_setup: WindowSetup) -> None:
    window_setup.square_height = ALLOWED_SQUARE_HEIGHTS[ALLOWED_SQUARE_HEIGHTS.index(window_setup.square_height)-1] #! FIXME: wrong indexing with smallest!

    _update(window_setup)
    
def _make_table_bigger(window_setup: WindowSetup, bigger_board_size: int) -> None:
    window_setup.square_height = bigger_board_size

    _update(window_setup)

def _get_next_board_size(window_setup: WindowSetup) -> int:
    current_board_size = ALLOWED_SQUARE_HEIGHTS.index(window_setup.square_height)
    
    if (current_board_size + 1) == len(ALLOWED_SQUARE_HEIGHTS):
        return current_board_size # this is the biggest we support

    return ALLOWED_SQUARE_HEIGHTS[current_board_size + 1]

def on_resize(window_setup: WindowSetup) -> None: # TODO: make sure to add option to disable this, at least partially
    new_size = window_setup.window.getmaxyx()
    current_board_size = window_setup.square_height
    bigger_board_size = _get_next_board_size(window_setup)

    if new_size[0] < get_board_height(current_board_size) or new_size[1] < get_board_width(current_board_size):
        _make_table_smaller(window_setup)

    if bigger_board_size > current_board_size:
        if new_size[0] >= get_board_height(bigger_board_size) and new_size[1] >= get_board_width(bigger_board_size):
            _make_table_bigger(window_setup, bigger_board_size)
