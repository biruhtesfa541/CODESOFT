from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def custom_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hi there! How can I assist you today?"
    elif "i need help with my order." in user_input:
        return "Sure! Please provide your order number."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how can i return a product?" in user_input:
        return "You can return a product within 30 days of purchase. Visit our returns page for more details."
    elif "what is your name" in user_input:
        return "my name is chatbot"
    elif "do you offer refunds?" in user_input:
        return "Yes, refunds are processed within 5-7 business days after receiving the returned product."
    elif "hi" in user_input:
        return "Hi, how can I help you?"
    

    else:
        return None

# Create chatbot
chatbot = ChatBot("MyBot")

# Train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)


print("Chatbot is ready! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = custom_response(user_input)
    if response:
        print(f"Chatbot: {response}")
    else:
        print(f"Chatbot: {chatbot.get_response(user_input)}")
