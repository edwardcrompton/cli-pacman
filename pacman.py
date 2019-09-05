import curses
import time

# Draw a class diagram to work out how to decouple the rendering and key input
# from the rest of the game logic.

class UserInterface:
    def __init__(self, board, pacman, scr):
        self.scr = scr
        self.pacman = pacman
        self.board = board
        self.renderer = CursesRenderer(self.board, self.pacman, self.scr)
        self.up = 'KEY_UP'
        self.down = 'KEY_DOWN'
        self.left = 'KEY_LEFT'
        self.right = 'KEY_RIGHT'

    def setUp(self):
        self.renderer.setUp()

    def tearDown(self):
        self.renderer.tearDown()

    def move(self, y, x):
        self.renderer.move(y, x)

    def scanDirection(self):
        c = self.scr.getkey()
        self.scr.addstr(15, 0, '                    ')
        self.scr.addstr(15, 0, c)

        if c == self.up:
            return (-1, 0)
        elif c == self.down:
            return (1, 0)
        elif c == self.left:
            return (0, 1)
        elif c == self.right:
            return (0, -1)
        else:
            return False

class CursesRenderer:
    def __init__(self, board, pacman, scr):
        self.board = board
        self.pacman = pacman
        self.wall = 9617
        self.food = 183
        self.scr = scr

    def setUp(self):
        self.scr.nodelay(True)
        self.scr.clear()

        self.renderInstructions()
        self.move(1, 1)

    def tearDown(self):
        curses.endwin()

    def renderBoard(self):
        layout = self.board.layout
        y = 0
        for row in layout:
            x = 0
            for square in row:
                tile = chr(self.wall) if square else chr(self.food)
                self.scr.addstr(y, x, tile)
                x = x + 1
            y = y + 1

    def renderInstructions(self):
        self.scr.addstr(12, 0, 'Use arrow keys to move. Press q to quit.')

    def move(self, y, x):
        posY = self.pacman.y + y
        posX = self.pacman.x + x

        if (posY >= 0 and posY < self.board.height and posX >= 0 and posX < self.board.width and self.board.allowed(posY, posX)):
            self.scr.addstr(self.pacman.y, self.pacman.x, ' ')
            self.scr.addstr(posY, posX, '@')

            self.pacman.y = posY
            self.pacman.x = posX

        self.scr.addstr(13, 0, 'Score: ' + str(self.board.points))

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

def main(scr):
    board = Board('board')
    pacman = Pacman()

    ui = UserInterface(board, pacman, scr)

    ui.setUp()
    ui.renderer.renderBoard()

    fps = 10
    lastFrameTime = time.time()

    while True:
        try:
            direction = ui.scanDirection()
            if direction:
                pacman.direction = direction

            ui.renderer.scr.addstr(14, 1, str(direction))
        except Exception as e:
            # No input
            pass

#        currentTime = time.time()
#        delta = currentTime - lastFrameTime
#        if delta >= 1/fps:
#            lastFrameTime = currentTime
#            ui.move(*pacman.direction)

curses.wrapper(main)

