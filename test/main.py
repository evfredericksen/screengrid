import win32api, win32con, win32gui, win32ui
import threading
import time
import string
import ctypes
import keyboard
import functools

from context import screengrid
import mouse

done = False

LETTERS = set(string.ascii_lowercase)

def foo():
    main_grid = screengrid.Grid()
    main_grid.draw_letter_grid()
    # s = time.time()
    # while time.time() - s < 10:
    #     win32gui.PumpWaitingMessages()

def main():
    threading.Thread(target=foo, daemon=True).start()
    input()

if __name__ == '__main__':
    main()