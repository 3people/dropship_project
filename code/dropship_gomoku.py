class Board:
    def __init__(self):
        self.board = [['+' for _ in range(20)] for _ in range(20)]
        self.startgame()


    def printboard(self) :
        print("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
        for x in range(20):
            print(str(x+1).rjust(2), end = " ")
            for y in range(20):
                print(str(self.board[x][y]).rjust(2), end=" " if y < 19 else "\n")

    def startgame(self):
        self.printboard()
        while True:
            x = int(input("player1의 x좌표를 입력하시오 : "))
            y = int(input("player1의 y좌표를 입력하시오 : "))
            self.board[x-1][y-1] = "●"
            self.printboard()
            if self.check(x-1,y-1,"●"):
                print("player1 win")
                break;
            x = int(input("player2의 x좌표를 입력하시오 : "))
            y = int(input("player2의 y좌표를 입력하시오 : "))
            self.board[x-1][y-1] = "○"
            if self.check(x-1,y-1,"○"):
                print("player2 win")
                break;
            self.printboard()

    def check(self, x, y, mark):
        a = []
        for n in range(1,5):
            a.append(eval("self.check"+str(n)+"("+str(x)+","+str(y)+",\""+mark+"\")"))
        if 5 in a:
            return True
        else :
            return False

    def check1(self, x, y, mark, d = 0):
        """가로방향"""
        if d == 0:
            return 1 + self.check1(x-1, y, mark, 1) + self.check1(x+1, y, mark, -1)
        elif d == 1:
            if self.board[x][y] == mark:
                return 1 + self.check1(x-1, y, mark, 1)
            else :
                return 0
        elif d == -1:
            if self.board[x][y] == mark:
                return 1 + self.check1(x+1, y, mark, -1)
            else :
                return 0

    def check2(self, x, y, mark, d = 0):
        """세로방향"""
        if d == 0:
            return 1 + self.check2(x, y+1, mark, 1) + self.check2(x, y-1, mark, -1)
        elif d == 1:
            if self.board[x][y] == mark:
                return 1 + self.check2(x, y+1, mark, 1)
            else :
                return 0
        elif d == -1:
            if self.board[x][y] == mark:
                return 1 + self.check2(x, y-1, mark, -1)
            else :
                return 0

    def check3(self, x, y, mark, d = 0):
        """\\대각선모양"""
        if d == 0:
            return 1 + self.check3(x-1, y-1, mark, 1) + self.check3(x+1, y+1, mark, -1)
        elif d == 1:
            if self.board[x][y] == mark:
                return 1 + self.check3(x-1, y-1, mark, 1)
            else :
                return 0
        elif d == -1:
            if self.board[x][y] == mark:
                return 1 + self.check3(x+1, y+1, mark, -1)
            else :
                return 0

    def check4(self, x, y, mark, d = 0):
        """//대각선모양"""
        if d == 0:
            return 1 + self.check4(x-1, y+1, mark, 1) + self.check4(x+1, y-1, mark, -1)
        elif d == 1:
            if self.board[x][y] == mark:
                return 1 + self.check4(x-1, y+1, mark, 1)
            else :
                return 0
        elif d == -1:
            if self.board[x][y] == mark:
                return 1 + self.check4(x+1, y-1, mark, -1)
            else :
                return 0

b = Board()
