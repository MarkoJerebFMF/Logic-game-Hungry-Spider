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
    # Naredimo glavno okno in nastavimo ime
    root = tkinter.Tk()
    root.title("Hungry Spider")
    # Naredimo objekt razreda Gui in ga spravimo v spremenljivko,
    # sicer bo Python mislil, da je objekt neuporabljen in ga bo pobrisal
    # iz pomnilnika.
    app = gameGui(root)
    # Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
    # delovati, ko okno zapremo.
    root.mainloop()



