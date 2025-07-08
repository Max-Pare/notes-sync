import colorama
from colorama import Fore, Back, Style
import random

colorama.init()
VERSION = '0.0.1'

def main():
    cprint('#' * 28, Fore.YELLOW)
    cprint('   ' + 'notesync version '+ VERSION, Fore.YELLOW)
    cprint('#' * 28, Fore.YELLOW)
    cprint('**WARNING** Webcam scan did not detect any trans or trans-adjacent pride flags in frame, '\
        'program functionality will be limited until your ally status is confirmed.', Fore.RED)
    if random.random() <= .43: print(' ' * random.randint(8, 65) + 'ACK!')

def cprint(string:str, col):
    print(col + string + Fore.WHITE)

if __name__ == '__main__':
    main()

