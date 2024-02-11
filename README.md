
# Sppq

Sppq — это универсальный пакет Python, предлагающий набор утилит для повышения производительности и автоматизации задач. От создания больших текстовых дисплеев до интеграции с GPT для обработки естественного языка — Sppq упрощает различные операции с помощью простого интерфейса Python.

## Оглавление

- [Установка](#Установка)
- [Применение](#Применение)
- [Функции](#Функции)
- [Примеры](#Примеры)

## Установка

Чтобы установить Sppq непосредственно из репозитория GitHub, используйте следующую команду:

```bash
pip install git+https://github.com/Sppqq/sppq.git@main
```

Чтобы обновить Sppq до последней версии:

```bash
pip install -U git+https://github.com/Sppqq/sppq.git@main
```

Для локальной установки:

1. Загрузите пакет
2. Разархивируйте пакет.
3. Откройте папку пакета в консоли.
4. Установите с помощью pip с файлом .whl:

```bash
pip install dist/sppq-**VERSION**-py3-none-any.whl
```

Замените `**VERSION**` актуальным номером версии Sppq, которую вы скачали.

## Применение

После установки пакета Sppq вы можете импортировать его в свой код Python, чтобы получить доступ к его функциям.

```python
from sppq import *
```

## Функции

Sppq предоставляет следующие функции

- `bigtext(text)`: Использует ASCII текст для вывода
- `cl()`: Очищает консоль
- `retell(url)`: Функция для обобщения или пересказа контента по заданному URL.
- `percent(one, two)`: Вычисляет процент одного числа к другому.
- `ask_gpt(prompt)`: Взаимодействует с GPT для предоставления ответов на запросы.
- `printt(text, speed)`: Медленная печать в консоль
- `pbarupdate(pb)`: Обновляет индикатор выполнения.
- `pbar()`: Инициализирует индикатор выполнения.
- `color2rgb('color')`: Переводит цвет в RGB
- `send_webhook(webhook_url, description, embed, file, title, color, author_name, author_url, author_icon_url, footer_text, footer_icon_url, thumbnail_url, username, avatar_url, content)`: Отправляет вебхук в дискорд

## Примеры

Вот несколько примеров использования библиотеки Sppq:

```python
from sppq import *
print(bigtext('Hello world!'))
```

```python
from sppq import *
printt('Hello world!')
```

```python
from sppq import *
print(ask_gpt('Как дела?'))
```

```python
from sppq import *
import time
pb = pbar(100)
for i in range(100):
    pbarupdate(pb)
    time.sleep(1)
```

```py
from sppq import *
printt(color2rgb('red'))
```
```py
printt(text=send_webhook('https://discord.com/api/webhooks/...'))
```