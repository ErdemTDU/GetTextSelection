
'''
def copy_clipboard():
    
    clipboard = Tk().clipboard_get()

    return clipboard

def copy_clipboard():
    #pyperclip.copy("") # <- This prevents last copy replacing  copy of .
    pya.hotkey('ctrl', 'c')
    time.sleep(1)  # ctrl-c is usually very  but your  may execute 
    return pyperclip.paste()

# double clicks on a position of  cursor
 
var = copy_clipboard()
print(var)

'''
import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time

def copy_clipboard():
    pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

# double clicks on a position of the cursor
#pya.doubleClick(pya.position())

list = []
var = copy_clipboard()
list.append(var) 
print(list)