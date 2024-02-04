import sppq
import pkg_resources
import requests
from bs4 import BeautifulSoup
import re
from sppq import functions

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


def printt(text: str, speed: float = .02, newLine=True):
    functions.printt(str(text), speed, newLine)

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:
    return functions.ask_gpt(prompt, model, stream)

def retell(url):
    return functions.retell(url)

def cl():
    functions.cl()
    return ''

def bigtext(text):
    return functions.bigtext(text)

def percent(num:float, denom:float):
    return functions.percent(num, denom)