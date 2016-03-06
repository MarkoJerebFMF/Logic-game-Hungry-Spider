# source code for Hungry Spider game, developed by Marko J. & Matija K.

import tkinter

GAME_HEIGHT = 400
GAME_WIDTH = 400
CIRCLERAD = 3
TOL = 8
CELLSIZE = 40
OFFSET = 10
DOTOFFSET = OFFSET + CIRCLERAD
PLAYER_ONE = "Player one"
PLAYER_TWO = "Player two"



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

    def start_game(self, playerOne, playerTwo):
        self.score = 0
        pass
    def finish_game(self,winner, score):
        pass
    def click(self, event):
        """ verifies where the mouse was clicked """
        pass
    def connectDots(self, xPos, yPos, orient):
        """ connects two dots """
        pass
    def isMoveValid(self,xPos, yPos, orient):
        pass
    def isClickClose(self, xPos, yPos):
        """verifies if the mouse click was close to the not connected dots"""
        pass
    def boxValue(self, xPos, yPos):
        pass
    def deleteMove(self,xPos, yPos, orient):
        pass







######################################################################
## Main Program

if __name__ == "__main__":

    root = tkinter.Tk()  # create Tk object, main window
    root.title("Hungry Spider")  # set window title

    app = gameGui(root)  # create gameGiu object in Tk window, we must! set the object in var.

    root.mainloop()  # we set control too main Tk window, mainloop stops when we select close window



