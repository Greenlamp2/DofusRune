import os
import win32api

import time
import win32con

from Dico import VK_CODE, press, pressAndHold, release
from clipboard import get_clipboard


class MouseEvent:

    def mousePos(self, cord):
        win32api.SetCursorPos((cord[0], cord[1]))

    def leftClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def leftDown(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        print('left Down')

    def leftUp(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(.1)

    def get_coords(self):
        x, y = win32api.GetCursorPos()
        print(x, y)

    def select_all(self):
        pressAndHold("ctrl")
        press("a")
        release("ctrl")

    def copier(self):
        pressAndHold("ctrl")
        press("c")
        release("ctrl")

    def coller(self):
        pressAndHold("ctrl")
        press("v")
        release("ctrl")

    def shift_click(self):
        pressAndHold("shift")
        time.sleep(.1)
        self.leftClick()
        time.sleep(.1)
        release("shift")

    def delete(self):
        press("del")

    def get_resultat_recherche(self):
        self.leftClick()
        self.mousePos((267, 220))
        self.shift_click()
        self.select_all()
        self.copier()
        self.delete()
        return get_clipboard()[1:-2]