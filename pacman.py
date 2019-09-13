import userinterface

class Board:
    def __init__(self, filename):
        self.width = 28
        self.height = 11
        self.points = 0

        self.layout = self.load(filename)

    def load(self, filename):
        file = open(filename, 'r')
        layout = []
        for row in file:
            line = []
            for square in row:
                if square in ['1', '0']:
                    line.append(int(square))

            layout.append(line)
        return layout

    def allowed(self, y, x):
        if self.layout[y][x] <= 0:
            if (self.layout[y][x] == 0):
                self.points = self.points + 100;
            self.layout[y][x] = -1
            return True
        else:
            return False

class Pacman:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.char = chr(64)
        self.direction = (0, -1)

board = Board('board')
pacman = Pacman()
game = userinterface.Game()
game.start(board,  pacman)
