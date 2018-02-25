import time

import sys

from excel import Excel
from item import Item
from listItem import ListItem
from ocrManager import OcrManager
from rechercheProcess import RechercheProcess
from screenManager import ScreenManager

def delete_png(items):
    for item in items:
        item.delete_png()


def get_list_by_type(item_type):
    if item_type == "run":
        return ListItem.runes
    elif item_type == "res":
        return ListItem.ressources
    else:
        return ListItem.test


def main():
    item_type = "test"
    count = 100
    if len(sys.argv) == 2:
        item_type = sys.argv[1]
    elif len(sys.argv) == 3:
        item_type = sys.argv[1]
        count = int(sys.argv[2])

    type = get_list_by_type(item_type)

    sm = ScreenManager()
    rp = RechercheProcess()
    r = Item()

    sm.set_focus_by_window_name("Greenlamp-Arrow")
    rp.search_multiple_item(type, count)

    items = r.generate_item_list(type)
    Excel(items, item_type)

    delete_png(items)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))