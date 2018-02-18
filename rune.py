import os

from PIL import Image


class Rune:
    def __init__(self, name=None):
        self.name = name
        self.price = 0

    def get_png(self):
        return self.name.replace(" ", "_")+ '.png'

    def delete_png(self):
        name =  self.name.replace(" ", "_")
        location = os.getcwd() + '\\' + name + '.png'
        os.remove(location)

    def resize_png(self):
        basewidth = 750
        img = Image.open(self.get_png())
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(self.get_png())
