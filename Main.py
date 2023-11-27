import json
import random_responses
import nltk
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import datetime

nltk.download('punkt')
nltk.download('wordnet')

def date():
    #!Store the current date and time
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time_str = current_datetime.strftime("%H:%M:%S")

    with open("bot.json", "r") as json_file:
        data = json.load(json_file)
    if data:
        current_date = ("Today date is " + date)
        data[0]["bot_response"] = current_date
        current_time = ("Today time is " + time_str)
        data[1]["bot_response"] = current_time
        current_dateAndtime = ("Today date and time is " + date + " " + time_str)
        data[2]["bot_response"] = current_dateAndtime
    with open("bot.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
        
#!Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)

#!Store JSON data
response_data = load_json("bot.json")

#!Name of BOT
bot_name = 'Bot'

#!Check the string that combine with number
def sentence_contain_string_with_number(input_string):
    pattern = r'[0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]+'
    match = re.search(pattern, input_string)
    return match is not None

# #!Check the string whether got error
# def sentence_contain_string_with_error(input_string):
#     spell = SpellChecker()
#     tokens = word_tokenize(input_string.lower())
#     for word in tokens:
#         if not spell.correction(word) == word:
#             return True
#     return False

#!Filter the user input and check error
def get_response(input_string):
    if sentence_contain_string_with_number(input_string):
        return "Your input should not combine a string and a number."
    
    # if sentence_contain_string_with_error(input_string):
    #     return "I noticed a spelling error in your input. Please check your spelling and try again."
    
    #!Create the empty list
    score_list = []
    new_list = []
    new_list1 = []

    #!Change input_string in to lowercase
    lower_string = input_string.lower()

    #!Tokenize the lower_string
    tokens = word_tokenize(lower_string)

    #!Spell Checking
    spell = SpellChecker()
    for word in tokens:
        new_list.append(spell.correction(word))
        print(new_list)
    
    lemmatizer = WordNetLemmatizer()
    for word in new_list:
        lematize = lemmatizer.lemmatize(word, 'v')
        new_list1.append(lematize)
        print(new_list1)

    #!Check all the response
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
    
        #!Check got any required words
        if required_words:
            for word in new_list1:
                if word in required_words:
                    required_score += 1
                
        #!Amount of required word must match the required score            
        if required_score == len(required_words):
            #!Check each word the user has input
            for word in new_list:
                #!If the word is in the respose, add to the score
                if word in response["user_input"]:
                    response_score += 1

        #!Add score to the list, debug it and find the best response
        score_list.append(response_score)

    #!Find the best response and return it if they are not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)
    
    #!Check if have SPECIFIC INPUT
    if input_string == "TTS ON":
        return "Text To Speech now ON"
    if input_string == "TTS OFF":
        return "Text To Speech now OFF"
    if input_string == 'quit' or input_string == 'QUIT':
        exit()
        
    #!Return a random response, if dont have good response
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        # start_time = time.time()
        print("Bot:", get_response(user_input))
        # end_time = time.time()
        # response_time = end_time - start_time
        # print(response_time)