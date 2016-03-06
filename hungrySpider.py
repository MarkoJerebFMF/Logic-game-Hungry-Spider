# source code for Hungry Spider game, developed by Marko J. & Matija K.

import tkinter

GAME_HEIGHT = 400
GAME_WIDTH = 400
CIRCLERAD = 3
TOL = 8
CELLSIZE = 40
OFFSET = 10
DOTOFFSET = OFFSET + CIRCLERAD



######################################################################
## Game

######################################################################
## Human player

######################################################################
## Computer player (min/max)

######################################################################
## Graphical User Interface

class gameGui():
    """Game Gui"""

    def __init__(self, master):
        menu = tkinter.Menu(master)  # main menu
        master.config(menu = menu)  # add main menu in the window







######################################################################
## Main Program

if __name__ == "__main__":

    root = tkinter.Tk()  # create Tk object, main window
    root.title("Hungry Spider")  # set window title

    app = gameGui(root)  # create gameGiu object in Tk window, we must! set the object in var.

    root.mainloop()  # we set control too main Tk window, mainloop stops when we select close window



