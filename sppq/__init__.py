import sppq
import pkg_resources
import requests
from bs4 import BeautifulSoup
import re
from sppq import functions
from sppq.functions import pbar, pbarupdate, printt, ask_gpt, percent, retell, cl, bigtext

def get_versions_from_filename():
    response = requests.get('https://api.github.com/repos/Sppqq/sppq/git/trees/main?recursive=1')
    soup = BeautifulSoup(response.text, 'html.parser')
    matches = re.findall(r'sppq-(.*?)-py3-none-any.whl', string=soup.text)
    return matches[-1]


def check_update():
    # Получаем установленную версию
    installed_version = pkg_resources.get_distribution("sppq").version
    # Получаем последнюю версию
    latest_version = get_versions_from_filename()
    sppq.cl()
    # Сравниваем версии
    if installed_version == latest_version:
        print('У вас установлена последняя версия')
    else:
        print(f"У вас установлена версия {installed_version}, но доступна новая версия {latest_version}. pip install git+https://github.com/Sppqq/sppq.git@main")