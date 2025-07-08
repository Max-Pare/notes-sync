import os
import pathlib
import shutil
from subprocess import Popen
import threading
import sys


FAKE_ARG = './test/myrepo'
repo_dir = ''

def main():
    print('\nInitializing ...\n'\
    '**WARNING** webcam scan did not detect any trans or trans-validating flags in frame, '\
        'program functionality will be limited until you confirm your ally status.')
    if FAKE_ARG:
        if len(sys.argv) > 1:
            sys.argv[1] = FAKE_ARG
        else:
            sys.argv.append(FAKE_ARG)
    print(sys.argv[1]) #debug
    repo_dir = sys.argv[1]
    r_validate_dir(repo_dir)
    repo_path = repo_prompt_create()
    print(repo_path)

def r_validate_dir(_path): # Methods beginning with r_ raise an exception 
    if not os.path.isdir(_path):
        if os.path.isfile(_path):
            raise FileNotFoundError('Not a directory.')
        raise FileNotFoundError('Directory does not exist.')

def repo_prompt_create() -> tuple[bool, pathlib.Path]:
    data = input('Enter complete repo path (e.g.: /home/notes/dirt shopping list): ')
    if len(data) > 1024: raise Exception('Path too long.') # this ain't C++ but whatever it's probably a good idea
    try:
        _p = pathlib.Path(data)
    except Exception as e:
        raise Exception(f'Invalid repo path ({str(e)})')
    return _p
    

if __name__ == '__main__':
    main()
