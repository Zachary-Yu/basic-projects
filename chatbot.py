def chatbot(input):
    if "hello" in input or "Hello" in input:
        return "Hello there! How may I assist you today"
    elif "bye" in input or "goodbye" in input:
        return "Have a good day"
    elif "sayonara" in input or "jaane" in input:
        return "Sayonara"
    else:
        return "I'm not sure how to respond to that"

name = str(input("What is your name? ")).strip().title()
x = input("What would you like to send to the chatbot? ")
result = chatbot(x)

print(f"{result}, {name}")