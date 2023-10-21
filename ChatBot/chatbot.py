import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there! What can I do for you?', 'Hey!']),
    (r'how are you?', ['I am good, thanks.', 'I am doing well.']),
    (r'(.*) your name?', ["I'm Zohaib.", "My name is Zohaib."]),
    (r'.*(help|assist).*', ["No, I don't have time for that.", "Go to school.", "I am not your teacher."]),
    (r'i am bored', ['Jump from the rooftop', "I can't help you", 'Chal bhaag', 'Go to space']),
    (r'knock.*', ["Who's there?", 'Boo.', 'Boo who?', "Don't cry, it's just a joke!","go home bro"]),
    (r'.*', ["I'm not sure I understand.", "Please ask another question."]),
    (r'quit', ['Goodbye!', 'Bye now.']),
]

chatbot = Chat(pairs, reflections)

print("Hello! I'm a chatbot made by Zohaib. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
