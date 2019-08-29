class Board:
    def __init__(self, filename):
        self.width = 28
        self.height = 2

        self.layout = self.load(filename)

    def render(self, wall, food):
        for row in self.layout:
            for square in row:
                tile = chr(wall) if square else chr(food)
                print (tile, end='')

            print ()

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

board = Board('board')
board.render(9617, 183)

