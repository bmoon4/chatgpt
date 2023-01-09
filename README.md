# ChatGPT libraries

## 1. ChatGPT-wrapper

Link: https://github.com/mmabrouk/chatgpt-wrapper

### Requirements

To use this repository, you will need to have the following packages installed:

`setuptools`: This package is used to create and manage Python packages.
You can install it using `pip install setuptools`.

### Installation

You can install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/mmabrouk/chatgpt-wrapper
```

This will install chatgpt-wrapper and it's dependencies.

Before starting the program, you will need to install a browser in playwright (if you haven't already).  The program will use firefox by default.

```
playwright install firefox
```

With that done, you should start up the program in `install` mode, which will open up a browser window.

```bash
chatgpt install
```

Log in to ChatGPT in the browser window, then stop the program.  After doing this, restart the program without the `install` parameter to begin using it.

### Example
![image](https://user-images.githubusercontent.com/28991527/211235794-28b4f850-1c6b-4f7d-b503-f2e32ab3649b.png)



## 2. pyChatGPT

Link: https://github.com/terry3041/pyChatGPT

### Installation

```bash
pip install -U pyChatGPT
```

### Usage

#### Obtaining session_token

1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.

![image](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)

#### Interactive mode

```bash
python3 -m pyChatGPT
```

```python
from pyChatGPT import ChatGPT

session_token ="YOUR_SESSION_TOKEN"
api = ChatGPT(session_token)


resp = api.send_message('Hello')
print(resp['message'])

api.reset_conversation()
```
![image](https://user-images.githubusercontent.com/28991527/211236235-2be9425b-69a6-42a3-b747-f8889bb68a02.png)

![image](https://user-images.githubusercontent.com/28991527/211236259-ae212c8e-c890-4e2e-b4e7-d8b34e0334e1.png)


## 3. ChatGPT (revChatGPT)

Link: https://github.com/acheong08/ChatGPT


### Installation

`pip3 install --upgrade revChatGPT`

### Configuration

Refer to the setup [guide](https://github.com/acheong08/ChatGPT/wiki/Setup) for more information.

### Usage

`python3 -m revChatGPT`

```python
from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
  "session_token": "<YOUR_TOKEN>"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("Prompt", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }
```


Example

```python
from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
  "session_token": "YOUR_SESSION_TOKEN",
}, conversation_id=None, parent_id=None) # You can start a custom conversation


question = 'Give me a sample Airflow DAG print hello world using python operator.' # The question to ask the bot

response = chatbot.ask(question, conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response['message']) # The response from the bot
```

![image](https://user-images.githubusercontent.com/28991527/211236623-22f82a2c-49eb-4036-b6d0-7eb6c885438c.png)


# Bonus: Auto-create a ppx with ChatGPT

Link: https://python-pptx.readthedocs.io/en/latest/user/quickstart.html

install `python-pptx` library

```bash
pip install python-pptx
```


```python
from chatgpt_wrapper import ChatGPT
import ppt_generator as utils

bot = ChatGPT()
question = "What is the meaning of life?"
response = bot.ask(question)
print(response)  # prints the response from chatGPT

# generate a ppt file
utils.ppt_generator(question, response)
```
![image](https://user-images.githubusercontent.com/28991527/211243884-73aa7a05-4ae8-43e8-8805-53c8baff317c.png)

![image](https://user-images.githubusercontent.com/28991527/211244053-2d5c52ba-9c18-4f2e-9df8-b36c615950ad.png)
![image](https://user-images.githubusercontent.com/28991527/211244071-4355bcc0-8a0f-4736-b0ab-7757d7d47dd5.png)
