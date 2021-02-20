import sys
from PIL import Image

import pytesseract
from pytesseract import image_to_string


class OcrManager:
    def __init__(self):
        pass

    """
    0 = Orientation and script detection (OSD) only.
    1 = Automatic page segmentation with OSD.
    2 = Automatic page segmentation, but no OSD, or OCR.
    3 = Fully automatic page segmentation, but no OSD. (Default)
    4 = Assume a single column of text of variable sizes.
    5 = Assume a single uniform block of vertically aligned text.
    6 = Assume a single uniform block of text.
    7 = Treat the image as a single text line.
    8 = Treat the image as a single word.
    9 = Treat the image as a single word in a circle.
    10 = Treat the image as a single character.
    """

    def ocr_image(self, image_location):
        location = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        pytesseract.tesseract_cmd = location
        image_file = image_location

        im = Image.open(image_file)
        text = "0"
        try:
            text = image_to_string(im)
            # text = image_to_string(im, config='-psm 7')
            # text = image_to_string(im, config='outputbase nobatch  digits')
            text = image_to_string(im, config='-psm 6')
        except IOError:
            sys.stderr.write('ERROR: Could not open file "%s"\n' % image_file)
            exit(1)
        text = self.dofus_treatment(text)
        print(text)
        return text

    def dofus_treatment(self, text):
        text = text.replace(" ", "")
        text = text.replace("K", "")
        text = text.replace("R", "")
        try:
            int(text)
        except:
            return "-1"
        return text