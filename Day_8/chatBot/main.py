def chatbot():
    print("Hello! I'm Alex. Ask me anything or type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Alex: Hello there! How can I assist you today?")
        elif user_input in ["how are you?", "how are you"]:
            print("Alex: I'm just code, but I'm running fine. Thanks for asking!")
        elif user_input in ["what is your name?", "what's your name","whats your name"]:
            print("Alex: I'm Alex, your friendly assistant.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Alex: Goodbye! Have a great day.")
            break
        else:
            print("Alex: Sorry, I didn’t understand that. Can you rephrase?")
 
if __name__ == "__main__":
    chatbot()
