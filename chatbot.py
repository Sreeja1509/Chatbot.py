import random

# Define responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "how_are_you": ["I'm doing well, thanks!", "I'm great, how about you?", "All good here!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I don't understand."]
}

def get_response(message):
    message = message.lower()
    
    if "hello" in message or "hi" in message:
        return random.choice(responses["greeting"])
    elif "how are you" in message:
        return random.choice(responses["how_are_you"])
    elif "goodbye" in message or "bye" in message:
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["default"])

def chat():
    print("Chatbot: Hello! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()cha
