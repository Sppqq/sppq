import sppq
from sppq import functions
import asyncio

async def check_update():
    last = functions.get_version_from_filename()
    now = sppq.__version__
    if last!= now:
        print(f'Версия: {now} - обновление доступно https://github.com/Sppqq/sppq/blob/main/dist/sppq-{last}-py3-none-any.whl')
    else:
        pass

def printt(text: str, speed: float = .02, newLine=True):
    asyncio.run(check_update())
    sppq.printt(text, speed, newLine)

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:
    asyncio.run(check_update())
    return sppq.ask_gpt(prompt, model, stream)

def retell(url):
    asyncio.run(check_update())
    return sppq.retell(url)
