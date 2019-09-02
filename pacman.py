import curses

# Draw a class diagram to work out how to decouple the rendering and key input
# from the rest of the game logic.

class UserInterface:
    def __init__(self, board, pacman):
        self.scr = curses.initscr()
        self.pacman = pacman
        self.board = board
        self.renderer = CursesRenderer(self.board, self.pacman, self.scr)
        self.up = 65
        self.down = 66
        self.left = 67
        self.right = 68

    def setUp(self):
        self.renderer.setUp()

    def tearDown(self):
        self.renderer.tearDown()

    def move(self, y, x):
        self.renderer.move(y, x)

    def waitForKeyPress(self):
        while True:
            c = self.scr.getch()
            if c == ord('q'):
                break
            elif c == self.up:
                self.move(-1, 0)
            elif c == self.down:
                self.move(1, 0)
            elif c == self.left:
                self.move(0, 1)
            elif c == self.right:
                self.move(0, -1)

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
        self.move(1, 1)

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
                self.stdscr.addstr(y, x, tile)
                x = x + 1
            y = y + 1

    def renderInstructions(self):
        self.stdscr.addstr(12, 0, 'Use arrow keys to move. Press q to quit.')

    def move(self, y, x):
        posY = self.pacman.y + y
        posX = self.pacman.x + x

        if (posY >= 0 and posY < board.height and posX >= 0 and posX < board.width and board.allowed(posY, posX)):
            self.stdscr.addstr(self.pacman.y, self.pacman.x, ' ')
            self.stdscr.addstr(posY, posX, '@')

            self.pacman.y = posY
            self.pacman.x = posX

        self.stdscr.addstr(13, 0, 'Score: ' + str(self.board.points))

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

board = Board('board')
pacman = Pacman()

ui = UserInterface(board, pacman)

ui.setUp()
ui.renderer.renderBoard()
ui.waitForKeyPress()
ui.tearDown()

