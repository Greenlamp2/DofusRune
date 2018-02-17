import os

import time
import xlsxwriter
from PIL import ImageGrab


def screenMe():
    box = (700, 400, 1090, 440)
    im = ImageGrab.grab(box)
    nom = os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png'
    im.save(nom, 'PNG')
    return nom

class Excel:
    def __init__(self, name="defaut"):
        self.workbook = xlsxwriter.Workbook(name + ".xlsx")
        self.worksheet = self.workbook.add_worksheet()
        self.active_column = 0
        self.active_row = 0

    def next_column(self):
        return self.active_column + 1

    def add_column(self, step=1):
        self.active_column += step

    def add_row(self, step=1):
        self.active_row += step

    def write(self, x, y, value):
        self.worksheet.write(x, y, value)

    def resize_column(self, col, size):
        self.worksheet.set_column(col, size)

    def resize_row(self, row, size):
        self.worksheet.set_row(row, size)

    def write_image(self, x, y, value):
        self.worksheet.insert_image(x, y, value)

    def empty_line(self):
        self.resize_row(self.active_row, 33)
        self.add_row()