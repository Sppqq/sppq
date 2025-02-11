import os
import time
# import g4f
# from g4f import Provider
# from g4f.client import Client
import requests
import asciitext as a
from tqdm import tqdm
from discord_webhook import DiscordWebhook
import matplotlib.colors as mcolors
from colorama import Fore

# client = Client()

# def str_to_class(classname):
#     classname = classname.lower()
#     if classname in 'g4f.models.gpt_35_turbo':
#         return g4f.models.gpt_35_turbo
#     elif classname in 'g4f.models.gpt_4':
#         return g4f.models.gpt_4
#     elif classname in 'copilot':
#         return 'Copilot'
#     else:
#         return classname

def ask_gpt(prompt: str, model='g4f.models.gpt_35_turbo', stream=None, provider=None) -> str:
    raise NotImplementedError
    # """
    # prompt string
    # model:
    #     gpt_35_turbo
    #     gpt_4
    #     copilot
    # stream: bool
    # """
    # if provider is None:
    #     model = str_to_class(model)

    #     if model == 'Copilot':
    #         model = "gpt-4"
    #         provider = Provider.Bing
    #     else:
    #         provider = Provider.Liaobots

    # stream = None
    # ignored = None
    # response = client.chat.completions.create(
    #     stream=stream,
    #     ignored=ignored,
    #     provider=provider,
    #     model=model,
    #     messages=[{"role": "user", "content": prompt}],
    # )
    # return response.choices[0].message.content


def retell(url: str) -> str:
    endpoint = 'https://300.ya.ru/api/sharing-url'
    response = requests.post(
        endpoint,
        json={'article_url': url},
        headers={
            'Authorization': 'OAuth y0_AgAAAAAwgCahAAoX4wAAAADzsA5heFqVG4hKTGKDW5CMJFkcJedAF-8'
        }
    )
    status = response.json().get('status')
    return response.json()['sharing_url'] if status == 'success' else 'https://300.ya.ru/'


def printt(text: str, speed: float = 0.02, newLine: bool = True) -> str:
    text = str(text)
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()
    return ''


def cl() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def bigtext(text: str, font_url: str = "https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/ANSI_Shadow.txt",
            color: str = "#ff0000") -> str:
    return a.asciii.asciitext(font_url, text.lower(), color)


def percent(num: float, denom: float) -> float:
    return num / denom * 100


def pbar(total: int) -> tqdm:
    return tqdm(total=total)


def pbarupdate(pbar: tqdm) -> None:
    pbar.update(1)


def color2rgb(color_input: str) -> tuple:
    return tuple([int(x * 255) for x in mcolors.to_rgb(color_input)])


def get_decimal_color(color_input: str | tuple) -> int | None:
    try:
        if isinstance(color_input, tuple) and len(color_input) == 3:
            return int('%02x%02x%02x' % color_input, 16)
        elif isinstance(color_input, str):
            rgb = tuple(color2rgb(color_input))
            return int('%02x%02x%02x' % rgb, 16)
    except Exception as e:
        print(f"{Fore.RED}ERROR:{Fore.RESET} {e}")
        return None


def _create_author(name: str, url: str = '', icon_url: str = '') -> dict:
    author = {'name': name}
    if url:
        author['url'] = url
    if icon_url:
        author['icon_url'] = icon_url
    return author


def _create_footer(text: str, icon_url: str = '') -> dict:
    footer = {'text': text}
    if icon_url:
        footer['icon_url'] = icon_url
    return footer


def create_embed(description: str = '', file: str = '', title: str = '', color: str = 'Red',
                author_name: str = '', author_url: str = '', author_icon_url: str = '',
                footer_text: str = '', footer_icon_url: str = '', thumbnail_url: str = '') -> dict:
    """Create Discord embed dictionary with provided parameters."""
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
        embed['author'] = _create_author(author_name, author_url, author_icon_url)

    if footer_text:
        embed['footer'] = _create_footer(footer_text, footer_icon_url)

    if thumbnail_url:
        embed['thumbnail'] = {'url': thumbnail_url}

    return embed


def send_webhook(
    webhook_url: str = '',
    description: str = '',
    embed: str = '',
    file: str = '',
    title: str = '',
    color: str = 'Red',
    author_name: str = '',
    author_url: str = '',
    author_icon_url: str = '',
    footer_text: str = '',
    footer_icon_url: str = '',
    thumbnail_url: str = '',
    username: str = 'SppqLib',
    avatar_url: str = 'https://d3f1iyfxxz8i1e.cloudfront.net/courses/course_image_variant/4492ffef8e09_w240.webp',
    content: str = 'Message from SppqLib'
) -> bool:
    """Send a message to Discord webhook with optional embed."""
    if not webhook_url:
        printt(f'{Fore.RED}Вы не указали webhook_url{Fore.RESET}')
        return False

    webhook = DiscordWebhook(
        url=webhook_url,
        username=username,
        avatar_url=avatar_url,
        content=content
    )

    embed_dict = create_embed(
        description, file, title, color,
        author_name, author_url, author_icon_url,
        footer_text, footer_icon_url, thumbnail_url
    )

    if embed_dict:
        webhook.add_embed(embed_dict)

    response = webhook.execute()
    return response.status_code == 200
