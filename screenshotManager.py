import os

from PIL import ImageGrab

from coord import Coord


class ScreenshotManager:
    def __init__(self):
        pass

    def screen_this(self, name, count):
        box = Coord.get_loc_prix(count)
        im = ImageGrab.grab(box)
        name_edited = os.getcwd() + '\\' + name.replace(" ", "_")+ '.png'
        im.save(name_edited, 'PNG')
        return name_edited