#!/usr/bin/env python3

import curses
from _curses import window as CursesWindow
from window_setup import WindowSetup
from console_drawing.main import draw_table
from console_drawing.event_handlers import on_resize
from typing import Dict, Callable, List


def event_loop(window_setup: WindowSetup) -> None:
    event_callbacks: Dict[int, List[Callable[[WindowSetup], None]]] = {
        curses.KEY_RESIZE: [on_resize]
    }

    while True:
        key = window_setup.window.getch()

        if key in event_callbacks:
            for event_callback in event_callbacks[key]:
                event_callback(window_setup)


def draw_wireframe_board(stdscr: CursesWindow):
    curses.curs_set(0)
    stdscr.clear()
    
    window_setup = WindowSetup(stdscr, 3)

    draw_table(window_setup)
    event_loop(window_setup)

curses.wrapper(draw_wireframe_board)
