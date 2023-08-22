# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


class Board:
    count = 0

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s" % (self.cells[1], self.cells[2], self.cells[3]))
        print("------------")
        print(" %s | %s | %s" % (self.cells[4], self.cells[5], self.cells[6]))
        print("------------")
        print(" %s | %s | %s" % (self.cells[7], self.cells[8], self.cells[9]))

    def update(self, cellno, player):
        if self.cells[cellno] == " ":
            self.cells[cellno] = player

    def Is_Winner(self, player):
        if (self.cells[1] == player and self.cells[2] == player and self.cells[3] == player
                or self.cells[1] == player and self.cells[4] == player and self.cells[7] == player
                or self.cells[1] == player and self.cells[5] == player and self.cells[9] == player
                or self.cells[2] == player and self.cells[5] == player and self.cells[8] == player
                or self.cells[3] == player and self.cells[6] == player and self.cells[9] == player
                or self.cells[4] == player and self.cells[6] == player and self.cells[5] == player
                or self.cells[7] == player and self.cells[3] == player and self.cells[5] == player):
            self.count += 1
            return True

    def Is_tie(self):
        filled_cell = 0
        for cell in self.cells:
            if cell != " ":
                filled_cell += 1
        if filled_cell == 9:
            return True

    def ai(self, player):
        if self.cells[5] == " ":
            self.update(5, player)
        else:
            for i in range(1, 10):
                if self.cells[i] == " ":
                    self.update(i, player)
                    break

    def rest(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()
print("welcome to our game")
board.display()


def refresh():
    os.system("cls")
    board.display()


while True:

    x_ch = int(input("\nX) Please choose 1 - 9 >"))
    board.update(x_ch, "X")
    refresh()
    if board.Is_tie():
        print("game end no one win")
        again = input("Would you like to play again Y/N >")
        if again == "Y":
            os.system("cls")
            board.rest()
            board.display()

        else:
            break
    if board.Is_Winner("X"):
        print("Player X win")
        again = input("Would you like to play again Y/N >")
        if again == "Y":
            os.system("cls")
            board.rest()
            board.display()
        else:
            break

    # o_ch = int(input("\nO) Please choose 1 - 9 >"))
    # board.update(o_ch, "O")
    board.ai("O")
    refresh()
    if board.Is_Winner("O"):
        print("Player O win")
        again = input("Would you like to play again Y/N >")
        if again == "Y":
            os.system("cls")
            board.rest()
            board.display()
        else:
            break
with open('result.txt', 'w') as f:
    sys.stdout = f
    print("player x win", board.count)
# Press the green button in the gutter to run the script.
