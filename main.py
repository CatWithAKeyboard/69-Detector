from PIL import ImageGrab
from PIL import ImageOps
import pytesseract
import tkinter as tk
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = ImageGrab.grab(bbox=None)
ImageOps.grayscale(cap)
health_str = pytesseract.image_to_string(cap, lang='eng')


def restart():
    while True:
        os.system('python main.py')
        exit()


window = tk.Tk()


def sixtynine_detected():
    msg = tk.Label(text='Nice.')
    msg.pack()


def detection():
    if '69' in health_str:
        sixtynine_detected()
        window.mainloop()

    else:
        restart()


detection()
