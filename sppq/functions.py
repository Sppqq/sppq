from g4f import ChatCompletion, get_model_and_provider, Provider
import g4f
import requests
import time
import os


def str_to_class(classname):
    if classname == 'g4f.models.gpt_35_turbo':
        return g4f.models.gpt_35_turbo 
    elif classname == 'g4f.models.gpt_4':
        return g4f.models.gpt_4

def ask_gpt(prompt:str, model='g4f.models.gpt_35_turbo', stream=None)->str:

    # Specify the provider manually
    provider = Provider.DeepInfra

    # Set the arguments for get_model_and_provider
    ignored = None
    # Include both "model" and "provider" arguments
    model, _ = get_model_and_provider(provider=provider, stream=stream, ignored=ignored, model=str_to_class(model))

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
    for i in text:  # Loop over the message
        # Print the one charecter, flush is used to force python to print the char
        print(i, end="", flush=True)
        time.sleep(speed)  # Sleep a little before the next one
    if newLine:  # Check if the newLine argument is set to True
        print()  # Print a final newline to make it act more like a normal print statement
    return ''

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')