import time

from clipboard import set_clipboard
from coord import Coord
from mouseEvent import MouseEvent
from screenshotManager import ScreenshotManager


class RechercheProcess:
    def __init__(self):
        self.me = MouseEvent()
        self.sm = ScreenshotManager()

    def search_single_item(self, name, count):
        time.sleep(.1)
        self.me.mousePos(Coord.loc_cancel)
        time.sleep(.1)
        self.me.leftClick()
        time.sleep(.1)
        self.me.mousePos(Coord.loc_recherche_box)
        time.sleep(.1)
        self.me.leftClick()
        time.sleep(.1)
        set_clipboard(name)
        time.sleep(.1)
        self.me.coller()
        time.sleep(.5)
        self.me.mousePos(Coord.loc_resultat)
        time.sleep(.1)
        self.me.leftClick()
        time.sleep(.5)
        self.sm.screen_this(name, count)


    def search_multiple_item(self, names, count):
        for name in names:
            self.search_single_item(name, count)
