from PIL import Image
import curses,os,sys
from time import sleep
os.system("mode con cols=65 lines=64")
line=os.path.dirname(__file__)
#line+='\\'+"black_white.png"
#line+='\\'+"test.ppm"
#print(line)
im=Image.open(line+'\\'+"next_test.ppm")
im=im.resize((64,64))
im=im.convert('P',palette=Image.ADAPTIVE, colors=8, dither=1)
im.save(line+'\\'+"new_test.png")
stdscr=curses.initscr()
curses.curs_set(0)
curses.start_color()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
pad=curses.newpad(64,65)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_CYAN)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLUE)
curses.init_pair(6, curses.COLOR_GREEN,curses.COLOR_GREEN)
curses.init_pair(7, curses.COLOR_BLACK,curses.COLOR_BLACK)
curses.init_pair(8, curses.COLOR_WHITE,curses.COLOR_WHITE)
for x in range(64):
    for y in range(64):
        if im.getpixel((x,y))==1:
            pad.addstr(y,x,'A',curses.color_pair(1))
        elif im.getpixel((x,y))==2:
            pad.addstr(y,x,'B',curses.color_pair(2))
        elif im.getpixel((x,y))==3:
            pad.addstr(y,x,'C',curses.color_pair(3))
        elif im.getpixel((x,y))==4:
            pad.addstr(y,x,'D',curses.color_pair(4))
        elif im.getpixel((x,y))==5:
            pad.addstr(y,x,'F',curses.color_pair(5))
        elif im.getpixel((x,y))==6:
            pad.addstr(y,x,'G',curses.color_pair(6))
        elif im.getpixel((x,y))==7:
            pad.addstr(y,x,'H',curses.color_pair(7))
        else:
            pad.addstr(y,x,'I',curses.color_pair(8))
pad.refresh(0,0,0,0,63,64)
sleep(30)
stdscr.getch()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
print("end")