import curses
from curses import wrapper


def start_screen(stdscr):
    """
    Displays the start screen of the Speed Typing Test.

    Args:
        stdscr (curses.window): The curses window object.
    """
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to start the test.")
    stdscr.refresh()
    stdscr.getkey()
    
    
def display_text(stdscr, target, current, wpm=0):
    """
    Function to display the target text and the current text typed by the user.

    Args:
        stdscr (curses.window): The curses window object.
        target (str): The target text to be typed by the user.
        current (str): The current text typed by the user.
        wpm (int): The words per minute (WPM) score of the user.
    """
    stdscr.addstr(target)
    
    for i, char in enumerate(current):
        stdscr.addstr(0, i, char, curses.color_pair(1))
    


def wpm_test(stdscr):
    """
    Function to perform a typing test using curses library.

    Args:
        stdscr (curses.window): The main window object of the curses library.
    """
    target_text = "Hello world this is some test text for this app"
    current_text = []

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)


def main(stdscr):
    """
    Main function that creates the screen, sets color pairs, displays start screen,
    and starts the word per minute (WPM) test.

    Args:
        stdscr (curses.window): The curses window object showing the screen.
    """
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
