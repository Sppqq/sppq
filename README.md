# Sppq

## [Сайт](https://jingle.bio/sppq/)

Установка

```bash
pip install git+https://github.com/Sppqq/sppq.git@main
```
Обновить
```bash
pip install -U git+https://github.com/Sppqq/sppq.git@main
```

Способ установки локально:

Скачать -> Распаковать -> Открыть папку в консоле -> Написать

```bash
pip install dist/sppq-**ВЕРСИЯ**-py3-none-any.whl
```



# Функции

- `bigtext(text)`
- `cl()`
- `retell(url)`
- `percent(one, two)`
- `ask_gpt(prompt)`
- `printt(text)`
- `pbarupdate(pb)`
- `pbar()`

# Примеры

```py
from sppq import *
print(bigtext('Hello world!'))
```
```py
from sppq import *
printt('Hello world!')
```
```py
from sppq import *
print(ask_gpt('Как дела?'))
```
```py
from sppq import *
import time
pb = pbar(100)
for i in range(100):
    pbarupdate(pb)
    time.sleep(1)
```
