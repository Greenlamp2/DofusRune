import xlsxwriter

from coord import Coord


class Excel:
    def __init__(self, items, name="defaut"):
        full_name = name + ".xlsx"
        print(full_name)
        self.workbook = xlsxwriter.Workbook(full_name)
        self.worksheet = self.workbook.add_worksheet()
        self.active_column = 0
        self.active_row = 0
        self.generate_item_excel(items)
        self.workbook.close()

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

    def generate_item_excel(self, items):
        self.resize_column('A:A', 15)
        self.resize_column('B:B', 15)
        self.resize_column('C:C', 17)
        self.resize_column('D:D', 18)
        i = 1
        for rune in items:
            print(str(i) + " / " + str(len(items)))
            self.write(self.active_row, self.active_column, rune.name)
            self.write_image(self.active_row, self.next_column(), rune.get_png())
            self.resize_row(self.active_row, Coord.size_row)
            self.add_row()
            self.write(self.active_row, self.next_column(), rune.price)
            self.add_row()
            i+=1