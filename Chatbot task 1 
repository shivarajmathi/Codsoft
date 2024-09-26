# Define the chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase to make it case-insensitive

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    # Asking about the chatbot
    elif "who are you" in user_input or "what are you" in user_input:
        return "I am a simple rule-based chatbot designed to assist you with basic queries."

    # Asking for help
    elif "help" in user_input:
        return "Sure, I can help! Please tell me what you need assistance with."

    # Asking about the weather
    elif "weather" in user_input:
        return "I'm unable to check live weather right now, but you can try checking a weather website."

    # Asking about time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    # Default response for unrecognized queries
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition for the chatbot
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Get chatbot response and display it
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
