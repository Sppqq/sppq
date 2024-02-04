import os

def get_files_from_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

files = get_files_from_directory('dist')
os.system('pip uninstall -y sppq')
os.system(f'pip install dist/{files[0]}')