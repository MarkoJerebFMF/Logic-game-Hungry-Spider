# source code for Hungry Spider game, developed by Marko J. & Matija K.

import tkinter

GAME_HEIGHT = 400
GAME_WIDTH = 400
DOTRAD = 3  #  radius of dots
CLICKAREA = 8  #  area for detecting mouse click
CELLSIZE = 40
OFFSET = 10
DOTOFFSET = OFFSET + DOTRAD
PLAYER_ONE = "Player one"
PLAYER_TWO = "Player two"
DOTSNUM = 5


######################################################################
## Game logic
######################################################################


######################################################################
##  Human player


class HumanPlayer():
    """class for creating a human player object"""

    def __init__(self, name, color = "black"):
        self.score = 0  # set score
        self.str = tkinter.StringVar()
        self.name = name
        self.color = color

    def update(self):
        """update StringVar on Frame"""
        self.str.set(self.name + ": %d" % self.score)


######################################################################
## Computer player (min/max)

class Computer():
    pass


######################################################################
## Graphical User Interface

class GameGui(tkinter.Frame):
    """Game Gui"""

    def __init__(self, master):
        tkinter.Frame.__init__(self, master)  # create Frame object

        menu = tkinter.Menu(master)  # main menu
        master.config(menu=menu)  # add main menu to the window

        play_menu = tkinter.Menu(menu)  # add play menu to master menu
        menu.add_cascade(label="Play", menu=play_menu)
        play_menu.add_command(label="Player 1 vs. Player 2", command=lambda: self.start_game(HumanPlayer, HumanPlayer))
        play_menu.add_command(label="Player 1 vs. Computer", command=lambda: self.start_game(HumanPlayer, Computer))
        play_menu.add_command(label="Computer vs. Player 1", command=lambda: self.start_game(Computer, HumanPlayer))
        play_menu.add_command(label="Computer vs. Computer", command=lambda: self.start_game(Computer, Computer))

        scoreH_menu = tkinter.Menu(menu)  # add score leader board to master menu
        menu.add_cascade(label="Score History", menu=scoreH_menu)
        scoreH_menu.add_command(label="Show Top 5 players", command=lambda: self.showScoreHistory())

        info_menu = tkinter.Menu(menu)  # add play instructions to master menu
        menu.add_cascade(label="Info", menu=info_menu)
        info_menu.add_command(label="How to play?", command=lambda: self.showGameInfo())

        game_menu = tkinter.Menu(menu)  # add game menu to master
        menu.add_cascade(label = "Game", menu = game_menu)
        game_menu.add_command(label = "Restart game!", command = lambda: self.restart_game())
        game_menu.add_command(label = "Quit game!", command = lambda: self.quit())

        self.canvas = tkinter.Canvas(self, height=GAME_HEIGHT, width=GAME_WIDTH)  # create canvas
        self.canvas.bind("<Button-1>", lambda e: self.click(e))  # bind mouse button 1 click to canvas
        self.canvas.grid(row=0, column=0)

        #  draw dots on canvas
        self.dots = [[self.canvas.create_oval(CELLSIZE * i + OFFSET,
                                              CELLSIZE * j + OFFSET,
                                              CELLSIZE * i + OFFSET + 2 * DOTRAD,
                                              CELLSIZE * j + OFFSET + 2 * DOTRAD,
                                              fill="black")
                      for j in range(DOTSNUM)] for i in range(DOTSNUM)]
        self.lines = []  # lines that connect dots

        self.grid()

    def start_game(self, playerOne, playerTwo):
        pass

    def finish_game(self):
        pass

    def restart_game(self):
        pass

    def click(self, event):
        """ verifies where the mouse was clicked """
        pass

    def connectDots(self, xPos, yPos, orient, currentPlayer):
        """ connects two dots, for current player """
        pass

    def isMoveValid(self, xPos, yPos, orient):
        pass

    def isClickClose(self, xPos, yPos):
        """verifies if the mouse click was close to the not connected dots"""
        pass

    def boxValue(self, xPos, yPos):
        pass

    def deleteMove(self, xPos, yPos, orient):
        pass

    def showScoreHistory(self):
        pass

    def showGameInfo(self):
        pass


######################################################################
## Main Program

if __name__ == "__main__":
    root = tkinter.Tk()  # create Tk object, main window
    root.title("Hungry Spider")  # set window title

    app = GameGui(root)  # create gameGiu object in Tk window, we must! set the object in var.
    root.mainloop()  # we set control too main Tk window, mainloop stops when we select close window
