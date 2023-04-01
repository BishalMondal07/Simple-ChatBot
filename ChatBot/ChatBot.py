import re
import random
from collections import defaultdict

import long_responses as long

# Define a dictionary to store responses
responses = defaultdict(list)

# Define a function to add responses to the dictionary
def add_response(user_input, bot_response, probability=1):
    responses[user_input].append((bot_response, probability))

# Define some standard responses
standard_responses = {
    'hello': ['Hello!', 'Hi there!', 'Hi!'],
    'how are you': ['I\'m doing well, thank you!', 'I\'m good. How are you?', 'I\'m great!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Bye!'],
    'thank you': ['You\'re welcome!', 'No problem!', 'Anytime!']
}

# Add the standard responses to the dictionary
for user_input, bot_responses in standard_responses.items():
    for bot_response in bot_responses:
        add_response(user_input, bot_response)

# Add some additional responses
add_response('what is your name', 'My name is Chatbot!')
add_response('how old are you', 'I\'m just a computer program, so I don\'t have an age!')
add_response('what can you do', 'I can answer questions and have conversations with you!')

# Define a function to get a response from the bot
def get_response(user_input):
    # Convert the user input to lowercase and split it into words
    words = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    # Initialize a dictionary to store the probabilities of each response
    probabilities = defaultdict(float)
    # Loop through the responses in the dictionary
    for user_response, bot_responses in responses.items():
        # Check if the user input contains the response
        if user_response in user_input:
            # Loop through the possible bot responses for the user input
            for bot_response, probability in bot_responses:
                # Calculate the probability of the bot response based on the words in the user input
                for word in words:
                    if word in bot_response.lower().split():
                        probabilities[bot_response] += probability / len(bot_responses)
                        break
    # If there are no matching responses, use a fallback response
    if not probabilities:
        return random.choice(long.unknown())
    # Otherwise, return the response with the highest probability
    return max(probabilities, key=probabilities.get)

# Start the chatbot
print('Chatbot: Hi! I\'m Chatbot. What can I help you with today?')
while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'goodbye']:
        print('Chatbot: Goodbye!')
        break
    bot_response = get_response(user_input)
    print('Chatbot:', bot_response)
