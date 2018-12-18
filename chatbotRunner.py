from __future__ import print_function
from chatbot import chatbot as bot
chatbot = bot()

statement = raw_input(bot.getGreeting(chatbot) + "\n")

while (statement.lower() != "bye"):
    print(bot.getResponse(chatbot, statement))
    statement = raw_input()