# Here is my attempt to create my first module:
#   A simple set of functions to print in colour in the terminal
#   SUGGESTION: import this module is "pr" or "prnt"

from functools import partial

colours = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'lightPurple': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'lightGrey': '\033[97m',
    'black': '\033[98m',
    'reset': '\033[00m'
}

def printInColour(colour, text):
    print(f'{colours[colour]} {text}{colours["reset"]}')

Red = partial(printInColour, 'red')
Green = partial(printInColour, 'green')
Yellow = partial(printInColour, 'yellow')
LightPurple = partial(printInColour, 'lightPurple')
Purple = partial(printInColour, 'purple')
Cyan = partial(printInColour, 'cyan')
LightGrey = partial(printInColour, 'lightGrey')
Black = partial(printInColour, 'black')
