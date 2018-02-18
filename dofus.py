import os
import re
import time

import win32gui

import psutil

import win32process

import sys
from PIL import ImageGrab, Image

import pytesseract
from clipboard import get_clipboard, set_clipboard
from coord import Coord
from excel import Excel
from mouseEvent import MouseEvent
from pytesseract import image_to_string
from rune import Rune
from windowMgr import WindowMgr

recherche_word = [
    "Rune Age",
    "Rune Cha",
    "Rune Fo",
    "Rune Ine",
    "Rune Pod",
    "Rune Vi",
    "Rune Sa",
    "Rune Pui",
    "Rune So",
    "Rune Do Air",
    "Rune Do Eau",
    "Rune Do Feu",
    "Rune Do Terre",

    "Rune Pa Age",
    "Rune Pa Cha",
    "Rune Pa Fo",
    "Rune Pa Ine",
    "Rune Pa Pod",
    "Rune Pa Vi",
    "Rune Pa Sa",
    "Rune Pa Pui",
    "Rune Pa So",
    "Rune Pa Do Air",
    "Rune Pa Do Eau",
    "Rune Pa Do Feu",
    "Rune Pa Do Terre",

    "Rune Ra Age",
    "Rune Ra Cha",
    "Rune Ra Fo",
    "Rune Ra Ine",
    "Rune Ra Pod",
    "Rune Ra Vi",
    "Rune Ra Sa",
    "Rune Ra Pui"
]

recherche_word2 = [
    "Rune Age",
    "Rune Cha",
    "Rune Fo",
    "Rune Ga Pa"
]

def recherche(nom):
    me = MouseEvent()
    time.sleep(.1)
    me.mousePos(Coord.loc_cancel)
    time.sleep(.1)
    me.leftClick()
    time.sleep(.1)
    me.mousePos(Coord.loc_recherche_box)
    time.sleep(.1)
    me.leftClick()
    time.sleep(.1)
    set_clipboard(nom)
    time.sleep(.1)
    me.coller()
    time.sleep(.5)
    me.mousePos(Coord.loc_resultat)
    time.sleep(.1)
    me.leftClick()
    time.sleep(.1)

def screenMe(nom):
    box = Coord.get_loc_prix()
    im = ImageGrab.grab(box)
    nom = os.getcwd() + '\\' + nom.replace(" ", "_")+ '.png'
    im.save(nom, 'PNG')
    return nom
windows = []

def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        windows.append(hwnd)



def put_dofus_front():
    w = win32gui
    p = w.GetWindowText(w.GetForegroundWindow())
    dofus = [item for item in psutil.process_iter() if item.name() == 'Dofus.exe']
    print(dofus)
    pid = next(item for item in psutil.process_iter() if item.name() == 'Dofus.exe').pid
    print(pid)
    win32gui.EnumWindows(enum_window_callback, pid)
    res = [win32gui.GetWindowText(item) for item in windows]
    print(res)
    name = res[0]
    we = WindowMgr()
    we.find_window_wildcard(".*"+name+".*")
    we.set_foreground()
    return 0

def start_retrieval(values):
    me = MouseEvent()
    time.sleep(.1)

    for value in values:
        recherche(value)
        time.sleep(.5)
        screenMe(value)


runes = []
def encapsulate_rune(values):
    for value in values:
        rune = Rune(value)
        rune.resize_png()
        runes.append(rune)

def generate_excel():
    excel = Excel("Runes")
    excel.resize_column('A:A', 15)
    excel.resize_column('B:B', 15)
    excel.resize_column('C:C', 17)
    excel.resize_column('D:D', 18)
    i = 1
    for rune in runes:
        print(str(i) + " / " + str(len(runes)))
        excel.write(excel.active_row, excel.active_column, rune.name)
        excel.write_image(excel.active_row, excel.next_column(), rune.get_png())
        excel.resize_row(excel.active_row, 170)
        excel.add_row()
        price = ocr_image(rune.get_png())
        excel.write(excel.active_row, excel.next_column(), price)
        excel.add_row()
        i+=1

def delete_png():
    for rune in runes:
        rune.delete_png()

def ocr_image(image_location):
    location = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    pytesseract.tesseract_cmd = location
    image_file = image_location

    im = Image.open(image_file)
    text = "0"
    try:
        text = image_to_string(im)
    except IOError:
        sys.stderr.write('ERROR: Could not open file "%s"\n' % image_file)
        exit(1)
    text = text.replace(" ", "")
    text = text.replace("K", "")
    text = text.replace("R", "")
    return int(text)


def main():
    #put_dofus_front()
    #start_retrieval(recherche_word)
    encapsulate_rune(recherche_word)
    generate_excel()
    #delete_png()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))