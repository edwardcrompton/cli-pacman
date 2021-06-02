import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
curses.curs_set(0)

stdscr.refresh()

stdscr.addstr(12, 0, "Press arrow keys to move, q to quit")

x = 0
y = 0
height = 10
width = 10

while True:
    c = stdscr.getch()

    xOld = x
    yOld = y
    move = False
    
    if c == ord('q'):
        break  # Exit the while()
    elif c == 65:
        if y > 0:
            y = y - 1
            move = True
    elif c == 66:
        if y < height:
            y = y + 1
            move = True
    elif c == 67:
        if x < width:
            x = x + 1
            move = True
    elif c == 68:
        if x > 0:
            x = x - 1
            move = True

    if move:
        stdscr.addstr(yOld, xOld, ' ')
        stdscr.addstr(y, x, '@')

curses.endwin()

