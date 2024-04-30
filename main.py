import curses
from curses import wrapper


def start_screen(stdscr):
    """
    Displays the start screen of the Speed Typing Test.

    Args:
        stdscr (curses.window): The curses window object.

    Returns:
        None
    """
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to start the test.")
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    """
    Function to perform a typing test using curses library.

    Args:
        stdscr (curses.window): The main window object of the curses library.

    Returns:
        None
    """
    target_text = "Hello world this is some test text for this app"
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
    
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
 
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
    Main function that initializes the curses screen, sets color pairs, displays the start screen,
    and starts the word per minute (WPM) test.

    Args:
        stdscr (curses.window): The curses window object representing the screen.

    Returns:
        None
    """
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)