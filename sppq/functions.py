import os
import time

try:
    from g4f import ChatCompletion, get_model_and_provider, Provider
    import g4f
except:
    os.system('pip install -U g4f')
try:
    import requests
except:
    os.system('pip install -U requests')

try:
    from asciitext import *
except:
    os.system('pip install -U asciitext')

try:
    from tqdm import tqdm
except:
    os.system('pip install -U tqdm')

try:
    from discord_webhook import DiscordWebhook
except:
    os.system('pip install -U discord_webhook')

try:
    import matplotlib.colors as mcolors
except:
    os.system('pip install -U matplotlib')

try:
    from colorama import Fore
except:
    os.system('pip install -U colorama')

def str_to_class(classname):
    if classname == 'g4f.models.gpt_35_turbo':
        return g4f.models.gpt_35_turbo 
    elif classname == 'g4f.models.gpt_4':
        return g4f.models.gpt_4

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:

    provider = Provider.DeepInfra

    ignored = None
    model, _ = get_model_and_provider(provider=provider, stream=stream, ignored=ignored, model=str_to_class(model))

    response = ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response

def retell(url):
    endpoint = 'https://300.ya.ru/api/sharing-url'
    response = requests.post(
        endpoint,
        json = {
        'article_url': url
        },
        headers = {'Authorization': 'OAuth y0_AgAAAAAwgCahAAoX4wAAAADzsA5heFqVG4hKTGKDW5CMJFkcJedAF-8'}
    )
    status = response.json().get('status')
    if status == 'success':
        url_ot = response.json()['sharing_url']
    else:
        url_ot = 'https://300.ya.ru/'
    return url_ot

def printt(text: str, speed: float = .02, newLine=True):
    text = str(text)
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()
    return ''

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

def bigtext(text, font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/ANSI_Shadow.txt", color="#ff0000"):
    return asciii.asciitext(font_url, text.lower(), color)

def percent(num, denom):
    return num / denom * 100

def pbar(total):
    return tqdm(total=total)

def pbarupdate(pbar: tqdm):
    pbar.update(1)

def color2rgb(color_input):
    return tuple([int(x*255) for x in mcolors.to_rgb(color_input)])

def get_decimal_color(color_input):
    try:
        if isinstance(color_input, tuple) and len(color_input) == 3:
            return int('%02x%02x%02x' % color_input, 16)
        elif isinstance(color_input, str):
            rgb = tuple(color2rgb(color_input))
            return int('%02x%02x%02x' % rgb, 16)
    except Exception as e:
        print(f"{Fore.RED}ERROR:{Fore.RESET} {e}")
        return None

def send_webhook(webhook_url=None, description = None, embed = None, file = None, title = None, color = None, author_name = None,
                 author_url = None, author_icon_url = None, footer_text = None, footer_icon_url = None, thumbnail_url = None,
                 username = None, avatar_url = None, content = None):
    if webhook_url is None:
        printt(f'{Fore.RED}Вы не указали webhook_url{Fore.RESET}')
    webhook = DiscordWebhook(url=webhook_url)
    if description is None and \
        embed is None and \
        file is None and \
        title is None and \
        color is None and \
        author_name is None and \
        author_url is None and \
        author_icon_url is None and \
        footer_text is None and \
        footer_icon_url is None and \
        thumbnail_url is None and \
        username is None and \
        avatar_url is None and \
        content is None:
        embed = {
            "username": "SppqLib (username параметр)",
            "avatar_url": "https://cdn.discordapp.com/avatars/758050281320742950/a_168ee7e42eb2937892c7533e7b5d1b6c.gif?size=1024",
            "content": "Content параметр",
            "title": 'Тестовое сообщение от из библиотеки sppq (title параметр)',
            "description": 'https://github.com/Sppqq/sppq/blob/main/README.md',
            "color": get_decimal_color('red'),
            "author": {
                "name": 'SppqLib (author параметр)',
                "url": '',
                "icon_url": 'https://cdn.discordapp.com/avatars/758050281320742950/a_168ee7e42eb2937892c7533e7b5d1b6c.gif?size=1024'
            },
            "fields": [
                {"name": '', "value": '', "inline": False},
            ],
            "thumbnail": {"url": ''},
            "image": {"url": ''},
            "footer": {"text": 'footer параметр'}
        }
        webhook.add_embed(embed)
        response = webhook.execute()
        if response.status_code == 200:
            return True
        else:
            return False
    else:
        embed = {
            "username": "",
            "avatar_url": "",
            "content": "",
            "title": '',
            "description": '',
            "color": '',
            "author": {
                "name": '',
                "url": '',
                "icon_url": ''
            },
            "fields": [
                {"name": '', "value": '', "inline": False},
            ],
            "thumbnail": {"url": thumbnail_url},
            "image": {"url": footer_icon_url},
            "footer": {"text": footer_text}
            }
    if description:
        embed['description'] = description
    if file:
        embed['file'] = file
    if title:
        embed['title'] = title
    if color:
        embed['color'] = get_decimal_color(color)
    if author_name:
        embed['author']['name'] = author_name
    if author_url:
        embed['author']['url'] = author_url
    if author_icon_url:
        embed['author']['icon_url'] = author_icon_url
    if footer_icon_url:
        embed['image']['url'] = footer_icon_url
    if footer_text:
        embed['footer']['text'] = footer_text
    if thumbnail_url:
        embed['thumbnail']['url'] = thumbnail_url
    if username:
        embed['username'] = username
    if avatar_url:
        embed['avatar_url'] = avatar_url
    if content:
        embed['content'] = content
    webhook.add_embed(embed)
    response = webhook.execute()
    if response.status_code == 200:
        return True
    else:
        return False
