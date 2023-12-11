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

def printInColour(text, colour):
    print(f'{colours[colour]} {text}{colours["reset"]}')


def Red(skk): print("\033[91m {}\033[00m" .format(skk))

def Green(skk): print("\033[92m {}\033[00m" .format(skk))

def Yellow(skk): print("\033[93m {}\033[00m" .format(skk))

def LightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def Purple(skk): print("\033[95m {}\033[00m" .format(skk))

def Cyan(skk): print("\033[96m {}\033[00m" .format(skk))

def LightGray(skk): print("\033[97m {}\033[00m" .format(skk))

def Black(skk): print("\033[98m {}\033[00m" .format(skk))
