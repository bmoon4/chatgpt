# https://github.com/acheong08/ChatGPT

from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
  "session_token": "YOUR_SESSION_TOKEN",
}, conversation_id=None, parent_id=None) # You can start a custom conversation


question = 'Give me a sample Airflow DAG print hello world using python operator.' # The question to ask the bot

response = chatbot.ask(question, conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response['message']) # The response from the bot
