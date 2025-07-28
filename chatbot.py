# Simple Python Chatbot using if-else

def simple_chatbot():
    print("🤖 Hello! I am your chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I help you?")
        elif 'name' in user_input:
            print("Bot: I am your simple Python chatbot.")
        elif 'how are you' in user_input:
            print("Bot: I'm just code, but I'm doing great! How about you?")
        elif 'bye' in user_input:
            print("Bot: Goodbye! Have a great day 😊")
            break
        else:
            print("Bot: I'm not sure I understand. Can you rephrase that?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()
