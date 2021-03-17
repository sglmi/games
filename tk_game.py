""" Creating a rock paper sccisors game with python 
    and tkinter 
"""

import random
import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk

from rps import get_winner, rand_hand


class Game:
    """ Main class to play the game. Logic part of the game. """

    def __init__(self, hand, dash):
        self.hand = hand
        self.dash = dash

    def play(self):
        computer = rand_hand(self.hand.HANDS)
        user = self.hand.name
        winner = get_winner(computer, user)
        dash.update(winner)
        return winner
        
class Hand:
    """ Player hand (rock, paper, scissors) """
    HANDS = ["Rock", "Paper", "Scissors"]

    def __init__(self, master, name, img):
        self.master = master
        self.name = name
        self.img = ImageTk.PhotoImage(Image.open(img))
    
    def show(self):
        label = ttk.Label(self.master, image=self.img) 
        label.pack(side=tk.LEFT)
        label.bind("<Button-1>", self.onclick)

    def onclick(self, event):
        game = Game(self)
        game.play() 

class Dashboard:
    """ Display the result of the game. """
    def __init__(self, master):
        self.master = master
        self.computer_wins = 0
        self.user_wins= 0
        self.ties = 0
    
    def show(self):
        ttk.Label(self.master, text="Game Result").pack()

    def update(self, result):
        """ Update dashboard based on winner. """
        if result == 0:
            self.ties += 1
        elif result == 1:
            self.user_wins += 1
        else:
            computer_wins += 1
        print(self.ties, self.computer_wins, self.user_wins)


def main():
    root = tk.Tk()
    root.title("ROCK PAPER SCISSORS")
    mainframe = ttk.Frame(root)

    rock = Hand(mainframe, "Rock", "./img/rock.png")
    paper = Hand(mainframe, "paper", "./img/paper.png")
    scissors = Hand(mainframe, "scissors", "./img/scissors.png")
    rock.show()
    paper.show()
    scissors.show()

    dashboard = Dashboard(mainframe)
    dashboard.show()
    
    mainframe.pack(fill=tk.BOTH)
    root.mainloop()


if __name__ == "__main__":
    main()

