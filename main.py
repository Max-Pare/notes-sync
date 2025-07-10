import colorama
from colorama import Fore, Back, Style
import random
import pathlib 
from time import sleep
import asyncio
import threading
from subprocess import Popen, STDOUT, DEVNULL
colorama.init()
VERSION = '0.0.2'
PERSISTENT_DATA_DIR='~/.notesync'
GIT_BIN = ''

repo_path = ''


def main():
    cprint('#' * 28, Fore.YELLOW)
    cprint('   ' + 'notesync version '+ VERSION, Fore.YELLOW)
    cprint('#' * 28, Fore.YELLOW)
    meme()
    init()

def meme():
    def _(delay: float):
        sleep(delay)
        cprint('**WARNING** Webcam scan did not detect any trans or trans-adjacent pride flags in frame, '\
            'program functionality will be limited until your ally status is confirmed.', Fore.RED)
    threading.Thread(target=_, args=((1 + random.random()),)).start()

def check_depenencies():
    '''Raises exception is crucial binaries aren\'t found,'''
    GIT_BIN = ''
    for bin in ['/bin/git','/usr/bin/git']:
        try:
            Popen([bin, '-v'], stdout=DEVNULL, stderr=DEVNULL)
            cprint('Git binary detected', Back.GREEN)
            GIT_BIN = bin
            break
        except Exception as e:
            cprint(str(e), Fore.YELLOW)
            continue
    if not GIT_BIN:
        cprint("GIT isn't installed or I failed to find it, if it's the latter then tough luck.", Fore.RED)
        exit(-1)    


def cprint(string:str, col=Fore.WHITE):
    print(col + string + Style.RESET_ALL)

def prompt_repo_path() -> tuple[bool, pathlib.Path]:
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

def prompt_yn(message:str):
    return input(message).strip().lower() in ('y', 'yes')

def init():
    check_depenencies()
    if repo_path:
        if not os.path.isdir(repo_path) and not os.path.isfile(repo_path):
            cprint(f'The cached repo no longer exists at path "{repo_path}", create a new one or specify the new path of the repo.', Fore.RED)
            cprint('TODO: implement this', Fore.GREEN)
        return
    repo_path = prompt_repo_path()





if __name__ == '__main__':
    main()

