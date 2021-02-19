import os

from PIL import Image

from coord import Coord
from ocrManager import OcrManager


class Item:
    def __init__(self, name=None):
        self.name = name
        self.price = 0
        self.om = OcrManager()

    def get_png(self):
        name_edited = os.getcwd() + '\\' + 'screenshots' + '\\' + self.name.replace(" ", "_")+ '.png'
        return name_edited

    def delete_png(self):
        name =  self.name.replace(" ", "_")
        location = os.getcwd() + '\\' + 'screenshots' + '\\' + self.name.replace(" ", "_")+ '.png'
        os.remove(location)

    def resize_png(self):
        basewidth = Coord.size_font
        img = Image.open(self.get_png())
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(self.get_png())

    def generate_item_list(self, names):
        items = []
        for name in names:
            item = Item(name)
            item.resize_png()
            item.get_ocr_price()
            items.append(item)

        return items

    def get_ocr_price(self):
        self.price = self.om.ocr_image(self.get_png())
        return self.price



