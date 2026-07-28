"""
CodeAlpha Python Internship - Task 4: Basic Chatbot
-----------------------------------------------------
A simple rule-based chatbot that replies to a few fixed user inputs.

Concepts used: if-elif, functions, loops, input/output
"""


def get_response(user_input):
    """Return a predefined reply based on keywords in the user's message."""
    message = user_input.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"
    elif "how are you" in message:
        return "I'm fine, thanks! How about you?"
    elif "your name" in message:
        return "I'm a simple chatbot built for the CodeAlpha internship."
    elif "help" in message:
        return "You can ask me things like 'hello', 'how are you', or say 'bye' to exit."
    elif message in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that. Try saying 'help' to see what I can do."


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' anytime to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    run_chatbot()