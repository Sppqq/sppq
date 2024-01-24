from g4f import ChatCompletion, get_model_and_provider, Provider
import g4f
import requests

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