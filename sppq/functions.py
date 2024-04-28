import os
import time

try: from g4f import ChatCompletion, get_model_and_provider, Provider; import g4f 
except: os.system('pip install -U g4f')

try: import requests 
except: os.system('pip install -U requests')

try: import asciitext as a
except: os.system('pip install -U asciitext')

try: from tqdm import tqdm 
except: os.system('pip install -U tqdm')

try: from discord_webhook import DiscordWebhook 
except: os.system('pip install -U discord_webhook')

try: import matplotlib.colors as mcolors
except: os.system('pip install -U matplotlib')

try: from colorama import Fore 
except: os.system('pip install -U colorama')

def str_to_class(classname):
    classname = classname.lower()
    if classname in 'g4f.models.gpt_35_turbo':
        return g4f.models.gpt_35_turbo
    elif classname in 'g4f.models.gpt_4':
        return g4f.models.gpt_4
    elif classname in 'copilot':
        return 'Copilot'
    else:
        raise ValueError(f'Unknown model: {classname}')

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:
    """
    prompt string
    model:
        gpt_35_turbo
        gpt_4
        copilot
    stream: bool
    """

    model = str_to_class(model)

    if model == 'Copilot':
        model = "gpt-4"
        provider = g4f.Provider.Bing
    else:
        provider = Provider.DeepInfra


    # Set the arguments for get_model_and_provider
    stream = None
    ignored = None
    # Include both "model" and "provider" arguments
    model, _ = get_model_and_provider(provider=provider, stream=stream, ignored=ignored, model=model)

    # Create the ChatCompletion object
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
    return a.asciii.asciitext(font_url, text.lower(), color)

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

def send_webhook(webhook_url='', description = '', embed = '', file = '', title = '', color = 'Red', author_name = '',
                 author_url = '', author_icon_url = '', footer_text = '', footer_icon_url = '', thumbnail_url = '',
                 username = 'SppqLib', avatar_url = 'https://d3f1iyfxxz8i1e.cloudfront.net/courses/course_image_variant/4492ffef8e09_w240.webp', content = 'Message from SppqLib'):
    if webhook_url is None:
        printt(f'{Fore.RED}Вы не указали webhook_url{Fore.RESET}')
        exit()
    embed = {}
    if description:
        embed['description'] = description
    if file:
        embed['file'] = file
    if title:
        embed['title'] = title
    if color != 'Red':
        embed['color'] = get_decimal_color(color)
    if author_name:
        embed['author'] = {'name': author_name}
    if author_url:
        embed['author']['url'] = author_url
    if author_icon_url:
        embed['author']['icon_url'] = author_icon_url
    if footer_text:
        embed['footer'] = {'text': footer_text}
    if footer_icon_url:
        embed['footer']['icon_url'] = footer_icon_url
    if thumbnail_url:
        embed['thumbnail'] = {'url': thumbnail_url}

    webhook = DiscordWebhook(url=webhook_url, username=username, avatar_url=avatar_url, content=content)
    if embed == {}:
        pass
    else:
        webhook.add_embed(embed)
    response = webhook.execute()
    if response.status_code == 200:
        return True
    else:
        return False
