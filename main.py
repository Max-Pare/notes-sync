import colorama
from colorama import Fore, Back, Style
import random
import pathlib 


colorama.init()
VERSION = '0.0.1'

local_repo = ''


def main():
    cprint('#' * 28, Fore.YELLOW)
    cprint('   ' + 'notesync version '+ VERSION, Fore.YELLOW)
    cprint('#' * 28, Fore.YELLOW)
    cprint('**WARNING** Webcam scan did not detect any trans or trans-adjacent pride flags in frame, '\
        'program functionality will be limited until your ally status is confirmed.', Fore.RED)
    if random.random() <= .43: print(' ' * random.randint(8, 65) + 'ACK!')

def cprint(string:str, col):
    print(col + string + Fore.WHITE)

def prompt_create_repo() -> tuple[bool, pathlib.Path]:
    data = input('Enter complete repo path (e.g.: /home/notes/dirt shopping list/): ')
    if len(data) > 1024:
        # probably a good idea
        cprint('Path too long', Fore.RED)
    try:
        _p = pathlib.Path(data)
    except Exception as e:
        raise Exception(f'Invalid repo path ({str(e)})')
    return _p

def validate_dir(_path):
    if not _path: return False 
    if not os.path.isdir(_path):
        if os.path.isfile(_path):
            raise FileNotFoundError('The path specified is a file, not a directory')
        return False
    return Tru1e


if __name__ == '__main__':
    main()

