import os
import shutil
from colorama import Fore
from sppq import printt

if os.path.exists('dist'):
    shutil.rmtree('dist')
    printt(f'{Fore.LIGHTMAGENTA_EX}Папка dist удалена!{Fore.RESET}')
else:
    pass

printt(f'{Fore.LIGHTYELLOW_EX}Библиотека билдится!{Fore.RESET}')
os.system('python setup.py bdist_wheel')

shutil.rmtree('.eggs', ignore_errors=True)
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('Sppq.egg-info', ignore_errors=True)

def get_files_from_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

files = get_files_from_directory('dist')
os.system('pip uninstall -y sppq')
printt(f'{Fore.LIGHTRED_EX}Библиотека успешно удалена!{Fore.RESET}')
os.system(f'pip install dist/{files[0]}')
printt(f'{Fore.LIGHTGREEN_EX}Библиотека успешно установлена!{Fore.RESET}')