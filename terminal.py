import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
curses.curs_set(0)

stdscr.refresh()

stdscr.addstr(1, 0, "Press q to quit")

x = 0
y = 0

while 1:
    c = stdscr.getch()

    stdscr.addstr(x, y, ' ')

    if c == ord('q'):
        break  # Exit the while()
    elif c == 65:
        stdscr.addstr(3, 0, 'Up')
        y = y - 1
    elif c == 66:
        stdscr.addstr(3, 0, 'Down')
        y = y + 1

    stdscr.addstr(x, y, '@')

curses.endwin()

