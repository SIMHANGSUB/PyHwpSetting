import win32api
import threading
import os, sys
import subprocess
import time

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def SaveFile(): # Ctrl + S 
    win32api.keybd_event(0x11,0,0,0) 
    time.sleep(0.1)
    win32api.keybd_event(0x53,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(0x53,0,0x0002,0)
    time.sleep(0.1)
    win32api.keybd_event(0x11,0,0x0002,0)

def ExitHwp(): # Alt + F4
    win32api.keybd_event(0x12,0,0,0) 
    time.sleep(0.1)
    win32api.keybd_event(0x73,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(0x73,0,0x0002,0)
    time.sleep(0.1)
    win32api.keybd_event(0x12,0,0x0002,0)


def main():

    time.sleep(3)
    
    for i in range(0,8):
        win32api.keybd_event(0x30,0,0,0)
        time.sleep(0.1)
       
    SaveFile()
    ExitHwp()

def open(filename):
    os.system(filename)



#root = Tk()
filename = askopenfilename(filetypes=[("Text files","*.hwp")])
#print ( filename )

threading.Thread(target = open , args = (filename,)).start()
main()
