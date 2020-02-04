import sys
from tkinter import Tk
import pyautogui as pya
import pyperclip
import time
from tkinter import messagebox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import Textgetgui
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def Translate(p1):
    print("Button clicked")
    sys.stdout.flush()

def getFromClipboard(top):
    pya.hotkey('ctrl', 'c')
    clipboard = root.clipboard_get()
    messagebox.showinfo("Translated Word", clipboard)
    messagebox.CANCEL

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    root.bind('<Control-g>', getFromClipboard)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Textgetgui
    Textgetgui.vp_start_gui()




