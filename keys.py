import curses
import os
import time

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    incrementor = 0
    fps = 10
    lastFrameTime = time.time()

    while True:
        try:                 
            key = win.getkey()         
            win.clear()                
            win.addstr("Detected key:")
           
            if key == 'q':
                break
            else:
                message = str(key)

            win.addstr(message) 
        except Exception as e:
            # No input
            pass

        currentTime = time.time()
        delta = currentTime - lastFrameTime
        if delta >= 1/fps:
            incrementor = incrementor + 1
            lastFrameTime = currentTime
            win.addstr(10, 0, 'Frames:' + str(incrementor))

curses.wrapper(main)
