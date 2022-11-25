class ticktacktoe():
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def gameboard(self):
        """display the board"""
        print(f"|{self.board[1]}| |{self.board[2]}| |{self.board[3]}|",
              f"|{self.board[4]}| |{self.board[5]}| |{self.board[6]}|",
              f"|{self.board[7]}| |{self.board[8]}| |{self.board[9]}|", sep="\n")
    def startgame(self, start=1):
        if start == 1:
            print("Tick-tack-toe!")
            self.gameboard()
            return self.move("X")
        else:
            return
    def tie_check(self):
        """check for tie"""
        tiecheck = self.board[1:]
        if " " in tiecheck:
            return False
        else:
            return True
    def rule_1(self, cell):
        """checks if cell is empty"""
        if self.board[cell] == " ":
            return True
        else:
            return False
    def win_cond(self, player):
        """define win conditions"""
        if self.board[1] == player and self.board[2] == player and self.board[3] == player:
            return True
        if self.board[4] == player and self.board[5] == player and self.board[6] == player:
            return True
        if self.board[7] == player and self.board[8] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        if self.board[3] == player and self.board[6] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True
        else:
            return False
    def reset(self):
        """reset game"""
        reset = input("Play again? (Y/N): ").upper()
        if reset == "Y":
            self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            return self.startgame()
        elif reset == "N":
            return self.startgame(0)
        else:
            return self.reset()
    def move(self, player):
        self.player = player
        if self.tie_check() == False:
            try:
                cell = int(input(f"Player {player}, choose number 1-9: "))
            except ValueError:
                print("Not valid")
                return self.move(player)
            if cell not in range(1,10):
                print("Not a valid move")
                return self.move(player)
            if self.rule_1(cell) == True:
                self.board[cell] = player
                self.gameboard()
                if self.win_cond(player) == True:
                    print(f"Player {player} wins!")
                    return self.reset()
                else:
                    if player == "X":
                        return self.move("O")
                    else:
                        return self.move("X")
            else:
                print("Not allowed")
                return self.move(player)
        else:
            print("It's a tie!")
            return self.reset()
ticktacktoe().startgame()