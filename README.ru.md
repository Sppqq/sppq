# 🚀 Sppq

[🇬🇧 English version](README.md)

> 🛠️ Универсальный пакет Python, предлагающий набор утилит для повышения производительности и автоматизации задач. От создания больших текстовых дисплеев до интеграции с GPT для обработки естественного языка — Sppq упрощает различные операции с помощью простого интерфейса Python.

## 📑 Оглавление

- [📥 Установка](#установка)
- [🔨 Применение](#применение)
- [⚙️ Функции](#функции)
- [💡 Примеры](#примеры)

## 📥 Установка

### 📦 Из PyPI (Рекомендуется)

```bash
pip install sppq
```

### 🔄 Из репозитория GitHub

```bash
pip install git+https://github.com/Sppqq/sppq.git@main
```

Чтобы обновить до последней версии:

```bash
pip install -U git+https://github.com/Sppqq/sppq.git@main
```

### 💾 Локальная установка

1. Загрузите пакет
2. Разархивируйте пакет
3. Откройте папку пакета в консоли
4. Установите с помощью pip с файлом .whl:

```bash
pip install dist/sppq-**VERSION**-py3-none-any.whl
```

> ℹ️ Замените `**VERSION**` актуальным номером версии Sppq, которую вы скачали.

## 🔨 Применение

После установки пакета Sppq вы можете импортировать его в свой код Python, чтобы получить доступ к его функциям:

```python
from sppq import *
```

## ⚙️ Функции

Sppq предоставляет следующие мощные функции:

### 📝 Текстовые и консольные операции
- `bigtext(text)`: ✨ Использует ASCII текст для вывода
- `cl()`: 🧹 Очищает консоль
- `printt(text, speed)`: ⌨️ Медленная печать в консоль

### 🤖 ИИ и обработка контента
- `retell(url)`: 📚 Обобщение или пересказ контента по заданному URL
- `ask_gpt(prompt)`: 🤔 Взаимодействует с GPT для получения ответов

### 📊 Утилиты
- `percent(one, two)`: 💯 Вычисляет процент одного числа к другому
- `pbar()`: 📊 Инициализирует индикатор выполнения
- `pbarupdate(pb)`: 🔄 Обновляет индикатор выполнения
- `color2rgb('color')`: 🎨 Переводит цвет в RGB

### 🔌 Интеграция
- `send_webhook(...)`: 📡 Отправляет сообщения через Discord webhook
  ```python
  send_webhook(
      webhook_url,      # URL Discord webhook
      description,      # Описание сообщения
      embed,           # Встраиваемый контент
      file,            # Прикрепляемый файл
      title,           # Заголовок сообщения
      color,           # Цвет встраиваемого контента
      author_name,     # Имя автора
      author_url,      # URL автора
      author_icon_url, # Иконка автора
      footer_text,     # Текст футера
      footer_icon_url, # Иконка футера
      thumbnail_url,   # Миниатюра
      username,        # Имя бота
      avatar_url,      # Аватар бота
      content          # Содержание сообщения
  )
  ```

## 💡 Примеры

Вот несколько примеров использования библиотеки Sppq:

### 🔤 Большой текст
```python
from sppq import *
print(bigtext('Hello world!'))
```

### ⌨️ Медленная печать
```python
from sppq import *
printt('Hello world!')
```

### 🤖 Взаимодействие с GPT
```python
from sppq import *
print(ask_gpt('Как дела?'))
```

### 📊 Индикатор выполнения
```python
from sppq import *
import time
pb = pbar(100)
for i in range(100):
    pbarupdate(pb)
    time.sleep(1)
```

### 🎨 Конвертация цвета
```python
from sppq import *
printt(color2rgb('red'))
```

### 📡 Discord Webhook
```python
from sppq import *
printt(text=send_webhook('https://discord.com/api/webhooks/...'))
``` 