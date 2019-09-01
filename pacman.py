import curses

# Draw a class diagram to work out how to decouple the rendering and key input
# from the rest of the game logic.
#
# At the moment 

class UserInterface:
    def __init__(self, board, pacman):
        scr = curses.initscr()
        self.pacman = pacman
        self.board = board
        self.renderer = CursesRenderer(self.board, self.pacman, scr)
        self.keyInput = Keys(scr)

    def setUp(self):
        self.renderer.setUp()

    def tearDown(self):
        self.renderer.tearDown()

    def move(self, y, x):
        self.renderer.move(y, x)

    def waitForKeyPress(self):
        key = self.keyInput.waitForKeyPress()

        if c == ord('q'):
            pass
        elif c == self.up:
            self.move(-1, 0)
        elif c == self.down:
            self.move(1, 0)

class CursesRenderer:
    def __init__(self, board, pacman, scr):
        self.board = board
        self.pacman = pacman
        self.wall = 9617
        self.food = 183
        self.stdscr = curses.initscr()

    def setUp(self):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.refresh()
        self.renderInstructions()

    def tearDown(self):
        curses.endwin()

    def renderBoard(self):
        layout = board.layout
        print(layout)
        y = 0
        for row in layout:
            x = 0
            for square in row:
                tile = chr(self.wall) if square else chr(self.food)
                print(x)
                print(y)
                self.stdscr.addstr(y, x, tile)
                x = x + 1
            y = y + 1

    def renderInstructions(self):
        self.stdscr.addstr(12, 0, 'Use arrow keys to move. Press q to quit.')

    def move(self, y, x):
        posY = self.pacman.y + y
        posX = self.pacman.x + x

        if (posY > 0 and posY < board.height and posX > 0 and posX < board.width):
            stdscr.addstr(self.pacman.y, self.pacman.x, ' ')
            stdscr.addstr(posY, posX, '@')

            self.pacman.y = posY
            self.pacman.x = posX

class Board:
    def __init__(self, filename):
        self.width = 28
        self.height = 11

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

class Pacman:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.char = chr(64)

class Keys:
    def __init__(self, scr):
        self.up = 65
        self.down = 66
        self.left = 67
        self.right = 68
        self.stdscr = scr

    def waitForKeyPress(self):
        while True:
            c = self.stdscr.getch()
            if (c == self.up or c == self.down or c == self.left or c == self.right):
                return c

board = Board('board')
pacman = Pacman()

ui = UserInterface(board, pacman)
ui.setUp()

ui.renderer.renderBoard()
ui.keyInput.waitForKeyPress()
ui.tearDown()

