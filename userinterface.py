import curses
import time

class CursesUserInterface:
    def __init__(self, board, pacman, scr):
        self.scr = scr
        self.pacman = pacman
        self.board = board
        self.renderer = CursesRenderer(self.board, self.pacman, self.scr)
        self.up = 'KEY_UP'
        self.down = 'KEY_DOWN'
        self.left = 'KEY_LEFT'
        self.right = 'KEY_RIGHT'
        self.quit = 'q'

    def setUp(self):
        self.renderer.setUp()

    def tearDown(self):
        self.renderer.tearDown()

    def move(self, y, x):
        self.renderer.move(y, x)

    def scanDirection(self):
        c = self.scr.getkey()

        if c == self.up:
            return (-1, 0)
        elif c == self.down:
            return (1, 0)
        elif c == self.left:
            return (0, -1)
        elif c == self.right:
            return (0, 1)
        else:
            return False

    def scanOption(self):
        c = self.scr.getKey()
        
        if c == self.quit:
            return 'QUIT'
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

class Game:
    def start(self,  board,  pacman):
        self.board = board
        self.pacman = pacman
        curses.wrapper(self.loop)

    def loop(self, scr):
        ui = CursesUserInterface(self.board, self.pacman, scr)

        ui.setUp()
        ui.renderer.renderBoard()

        fps = 8
        lastFrameTime = time.time()

        while True:
            try:
                direction = ui.scanDirection()
                if direction:
                    self.pacman.direction = direction

                ui.renderer.scr.addstr(14, 1, str(direction))
            except Exception as e:
                # No input
                pass

            try:
                option = ui.scanOption()
                if option == 'QUIT':
                    break
            except Exception as e:
                #No input
                pass

            currentTime = time.time()
            delta = currentTime - lastFrameTime
            if delta >= 1/fps:
                lastFrameTime = currentTime
                ui.move(*self.pacman.direction)
