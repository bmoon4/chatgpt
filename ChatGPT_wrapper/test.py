# https://github.com/mmabrouk/chatgpt-wrapper
from chatgpt_wrapper import ChatGPT
import ppt_generator as utils

bot = ChatGPT()
question = "What is the meaning of life?"
response = bot.ask(question)
print(response)  # prints the response from chatGPT

# generate a ppt file
utils.ppt_generator(question, response)