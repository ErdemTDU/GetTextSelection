import sys
from tkinter import Tk
import pyautogui as pya
import pyperclip
import time
from tkinter import messagebox
from tkinter import *
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
    toplevel = Toplevel()
    toplevel.title('Info')
    pya.hotkey('ctrl', 'c')
    clipboard = root.clipboard_get()
    Message(toplevel, text=clipboard, padx=20, pady=20).pack()
    toplevel.after(2000, toplevel.destroy)
    

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




