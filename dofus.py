import sys
import time

from excel import Excel
from item import Item
from listItem import ListItem
from rechercheProcess import RechercheProcess
from screenManager import ScreenManager

def delete_png(items):
    for item in items:
        item.delete_png()


def get_list_by_type(item_type):
    liste =  ListItem.get_list(item_type)
    if liste == None or liste == []:
        liste = ListItem.test
    return liste


def main():
    item_type = "test"
    count = 100
    if len(sys.argv) == 2:
        item_type = sys.argv[1]
    elif len(sys.argv) == 3:
        item_type = sys.argv[1]
        count = int(sys.argv[2])

    type = get_list_by_type(item_type)
    execution(type, count, item_type)

def execution(type, count, item_type):
    sm = ScreenManager()
    rp = RechercheProcess()
    r = Item()

    sm.set_focus_by_window_name("new 1")
    rp.search_multiple_item(type, count)

    items = r.generate_item_list(type)
    Excel(items, item_type)

    delete_png(items)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))