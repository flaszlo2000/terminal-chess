#!/usr/bin/env python3

import curses
from _curses import window as CursesWindow
from window_setup import WindowSetup
from console_drawing.main import draw_table
from console_drawing.event_handlers import on_resize
from typing import Dict, Callable, List
from console_drawing.coord import Coord
from table.table import Table


def move_piece_up(window_setup: WindowSetup) -> None:
    window_setup.table.move_piece(Coord(1, 7), Coord(2, 5))
    draw_table(window_setup)

def event_loop(window_setup: WindowSetup) -> None:
    event_callbacks: Dict[int, List[Callable[[WindowSetup], None]]] = {
        curses.KEY_RESIZE: [on_resize],
        curses.KEY_UP: [move_piece_up]
    }

    while True:
        key = window_setup.window.getch()

        if key in event_callbacks:
            for event_callback in event_callbacks[key]:
                event_callback(window_setup)


def draw_wireframe_board(stdscr: CursesWindow):
    curses.curs_set(0)
    stdscr.clear()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, 243) #! FIXME: add correct black color

    window_setup = WindowSetup(stdscr, Table.create(), 1)
    on_resize(window_setup) # initial resize # TODO: make sure to add option to disable this

    draw_table(window_setup)
    event_loop(window_setup)

curses.wrapper(draw_wireframe_board)
