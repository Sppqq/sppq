import requests

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