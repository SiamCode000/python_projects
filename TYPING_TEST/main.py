import curses
from curses import wrapper
import time
import random
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to The typing test Game!")
    stdscr.addstr("\npress any key to start")
    stdscr.refresh()
    stdscr.getkey()


def show_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(f"\nWPM:{wpm}")
    for i,char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0,i, char,color)

def load_text():
    with open("text.txt","r") as f:
        lines = f.readlines()
    return random.choice(lines)


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_Time = time.time()
    stdscr.nodelay(True)

   
    while True:
        time_elacsped = max(time.time() - start_Time,1)
        wpm = round((len(current_text) / (time_elacsped/60)) / 5)
        stdscr.clear()
        show_text(stdscr,target_text,current_text,wpm)
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
       
        stdscr.refresh()

        try:
            key =  stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text): 
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    start_screen(stdscr)
    while  True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"press any key to continue")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)