import pynput
import os
from pynput.keyboard import Key, Listener

pointer = 0
LIST = ['   first', '   second', '   third', '   fourth', '   fifth', '   sixth']
def list(dir):
    global pointer
    os.system('CLS')
    if dir == 1:
        LIST[pointer] = LIST[pointer].replace("*","")
        pointer = pointer - 1
    
    if dir == 2:
        LIST[pointer] = LIST[pointer].replace("*","")
        pointer = pointer + 1

    if pointer == 6:
        pointer = 0

    if pointer == -1:
        pointer = 5

    for x in range(len(LIST)):
        if x == pointer:
            LIST[x] = '*' + LIST[x]
        print(LIST[x])

    return pointer

def showcase ():
    global pointer
    os.system('CLS')
    print(LIST[pointer])

def on_press(key):
    if key == Key.up:
        pointers = list(1)
    elif key == Key.down:
        pointers = list(2)
    elif key == Key.enter:
        showcase()
    if key == Key.esc:
        return False

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

