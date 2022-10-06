import sys
from PyQt5 import QtWidgets, QtQuick, QtCore

from tkinter import Tk
from tkinter import Canvas
from tkinter import ttk

class MainScreen:
    def __init__(this):
        this.window = Tk()
    
    def setSize(this,w,h):
        this.width = w
        this.height = h
        this.window.geometry(str(w)+"x"+str(h))
        
    def setBackground(this,color):
        this.window.configure(background = color)
        
    def getInfo(this):
        return this.configure().keys()
    
    def setResizable(this,resizable):
        this.window.resizable(resizable, resizable)
        
    def setTitle(this,title):
        this.window.title(title)
        
    def run(this):
        this.window.mainloop()

class MainCanvas:
    def __init__(this,w,h,bg):
        this.canvas = Canvas(width = w, height = h, bg = bg)
        this.padding = {}
    
    def setPadding(this,internal,x,y=None):
        if internal == True:
            this.padding['ipadx'] = x
            this.padding['ipady'] = y if y else x
        else:
            this.padding['padx'] = x
            this.padding['pady'] = y if y else x
    
    def putIn(this):
        exec("this.canvas.pack("+str(this.padding).replace("'","").replace(":","=").replace("{","").replace("}","")+")")
            

def createWindow():
    wind = MainScreen()
    wind.setSize(400,400)
    wind.setBackground("grey")
    wind.setTitle("Canvas - Draw Shapes")
    
    wind.setResizable(False)
    
    canvas = MainCanvas(350, 350, "white")
    canvas.setPadding(True, 20)
    canvas.putIn()
     
    wind.run()



if __name__ == '__main__':
    createWindow()