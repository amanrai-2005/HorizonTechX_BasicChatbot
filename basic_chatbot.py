def chatbot():
    print("🤖 Simple Chatbot")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! How can I help you today?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user_input in ["i am fine", "i'm fine", "good"]:
            print("Bot: That's great to hear!")

        elif user_input == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Run the chatbot
chatbot()