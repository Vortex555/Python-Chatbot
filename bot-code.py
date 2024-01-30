from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
bot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = bot.get_response(user_input)
    print(f"MyBot: {response}")
