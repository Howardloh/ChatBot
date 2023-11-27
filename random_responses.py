import random

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terriblt sorry, I didn't quite catch that.",
        "I apologize, but your request is outside my current capabilities.",
        "I'm not sure what you mean. Could you provide more details?",
        "Let's try that again. What can I help you with?",
        "I can't answer that yet, please try asking something else."
    ]
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    return random_list[random_item]