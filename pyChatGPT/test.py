# https://github.com/terry3041/pyChatGPT

from pyChatGPT import ChatGPT

session_token ="YOUR_SESSION_TOKEN"
api = ChatGPT(session_token)

resp = api.send_message('Hello')
print(resp['message'])

api.reset_conversation()
