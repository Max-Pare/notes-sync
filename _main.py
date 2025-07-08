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
    '**WARNING**: webcam scan did not detect any trans or trans-validating flags in frame, '\
        'program functionality will be limited until you confirm your ally status.')
    if FAKE_ARG:
        if len(sys.argv) > 1:
            sys.argv[1] = FAKE_ARG
        else:
            sys.argv.append(FAKE_ARG)
    print(sys.argv[1]) #debug
    repo_dir = sys.argv[1]
    while not validate_dir(repo_dir):
        repo_dir = prompt_create_repo()
    print(repo_path)

def prompt_create_repo() -> tuple[bool, pathlib.Path]:
    data = input('Enter complete repo path (e.g.: /home/notes/dirt shopping list/): ')
    if len(data) > 1024: raise Exception('Path too long.') # probably a good idea
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
    return True

if __name__ == '__main__':
    main()
