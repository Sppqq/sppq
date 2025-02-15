# 🚀 Sppq

[🇷🇺 Русская версия](README.ru.md)

> 🛠️ A versatile Python package offering a set of utilities to enhance productivity and automate tasks. From creating large text displays to integrating with GPT for natural language processing, Sppq simplifies various operations through a simple Python interface.

## 📑 Table of Contents

- [📥 Installation](#installation)
- [🔨 Usage](#usage)
- [⚙️ Functions](#functions)
- [💡 Examples](#examples)

## 📥 Installation

### 📦 From PyPI (Recommended)

```bash
pip install sppq
```

### 🔄 From GitHub Repository

```bash
pip install git+https://github.com/Sppqq/sppq.git@main
```

To update to the latest version:

```bash
pip install -U git+https://github.com/Sppqq/sppq.git@main
```

### 💾 Local Installation

1. Download the package
2. Unzip the package
3. Open the package folder in the console
4. Install using pip with the .whl file:

```bash
pip install dist/sppq-**VERSION**-py3-none-any.whl
```

> ℹ️ Replace `**VERSION**` with the actual version number of Sppq you downloaded.

## 🔨 Usage

After installing the Sppq package, you can import it into your Python code to access its functions:

```python
from sppq import *
```

## ⚙️ Functions

Sppq provides the following powerful functions:

### 📝 Text and Console Operations
- `bigtext(text)`: ✨ Uses ASCII text for output
- `cl()`: 🧹 Clears the console
- `printt(text, speed)`: ⌨️ Slow printing to console

### 🤖 AI and Content Processing
- `retell(url)`: 📚 Summarizes or retells content from a given URL
- `ask_gpt(prompt)`: 🤔 Interacts with GPT for responses

### 📊 Utilities
- `percent(one, two)`: 💯 Calculates percentage between numbers
- `pbar()`: 📊 Initializes a progress bar
- `pbarupdate(pb)`: 🔄 Updates the progress bar
- `color2rgb('color')`: 🎨 Converts color to RGB

### 🔌 Integration
- `send_webhook(...)`: 📡 Sends messages through Discord webhook
  ```python
  send_webhook(
      webhook_url,      # Discord webhook URL
      description,      # Message description
      embed,           # Embed content
      file,            # File attachment
      title,           # Message title
      color,           # Embed color
      author_name,     # Author name
      author_url,      # Author URL
      author_icon_url, # Author icon
      footer_text,     # Footer text
      footer_icon_url, # Footer icon
      thumbnail_url,   # Thumbnail
      username,        # Bot username
      avatar_url,      # Bot avatar
      content          # Message content
  )
  ```

## 💡 Examples

Here are some examples to get you started with Sppq:

### 🔤 Big Text Display
```python
from sppq import *
print(bigtext('Hello world!'))
```

### ⌨️ Slow Printing
```python
from sppq import *
printt('Hello world!')
```

### 🤖 GPT Interaction
```python
from sppq import *
print(ask_gpt('How are you?'))
```

### 📊 Progress Bar
```python
from sppq import *
import time
pb = pbar(100)
for i in range(100):
    pbarupdate(pb)
    time.sleep(1)
```

### 🎨 Color Conversion
```python
from sppq import *
printt(color2rgb('red'))
```

### 📡 Discord Webhook
```python
from sppq import *
printt(text=send_webhook('https://discord.com/api/webhooks/...'))
```
