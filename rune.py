import os


class Rune:
    def __init__(self, name=None):
        self.name = name

    def get_png(self):
        return self.name.replace(" ", "_")+ '.png'

    def delete_png(self):
        name =  self.name.replace(" ", "_")
        location = os.getcwd() + '\\' + name + '.png'
        os.remove(location)
