import re
import random

# define a function to generate responses
def get_response(user_input):
    # convert user input to lowercase
    user_input = user_input.lower()

    # extract information using regular expressions
    match = re.search(r'hi|hello|hey', user_input)
    if match:
        responses = ["Hi there!", "Hello!", "Hey!"]
        return random.choice(responses)
    
    match = re.search(r'what is your name', user_input)
    if match:
        return "My name is Chatbot"
    
    match = re.search(r'my name is (.+)', user_input)
    if match:
        name = match.group(1)
        responses = ["Nice to meet you, " + name + "!", "Hello, " + name + "!"]
        return random.choice(responses)
    
    match = re.search(r'joke|funny|laugh', user_input)
    if match:
        jokes = ["Why did the tomato turn red? Because it saw the salad dressing!", 
                 "Why did the chicken cross the playground? To get to the other slide!", 
                 "What do you call a bear with no teeth? A gummy bear!"]
        return random.choice(jokes)
    
    # generate longer responses
    greetings = ['Hello!', 'Hi!', 'Hey there!', 'Howdy!', 'Greetings!']
    topics = ['weather', 'food', 'movies', 'books', 'travel', 'music']
    questions = ['How are you today?', 'What have you been up to?', 'What do you think of the ' + random.choice(topics) + '?']
    responses = ['I am a chatbot and I do not have emotions, but thank you for asking!', 
                 'I am here to assist you with your needs. How can I help you today?', 
                 'I am programmed to talk about a variety of topics, such as ' + ', '.join(topics) + '. What would you like to discuss?', 
                 'I am sorry, I did not understand your question. Could you please rephrase it?', 
                 'Interesting, tell me more about that.']
    if user_input.endswith('?'):
        return random.choice(questions)
    else:
        return random.choice(greetings) + ' ' + random.choice(responses)

# main loop
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
