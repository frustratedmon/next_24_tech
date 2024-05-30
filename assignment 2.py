import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"how are you?",
        ["Good How about You!!!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that!",]
    ],
    [
        r"(.*) age?",
        ["I am a timeless entity.",]
    ],
    [
        r"(.*) created you?",
        ["I was assigned by Next24Technology and created by Surya2004.",]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm in the cloud, everywhere and nowhere!",]
    ],
    [
        r"how can I (.*)",
        ["You can start by telling me what you need help with.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you please rephrase?"]
    ]
]

chatbot = Chat(pairs, reflections)

def chatbot_interface():
    print("Hi! I am a chatbot created to assist you. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_interface()


