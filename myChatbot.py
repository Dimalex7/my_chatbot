import re

def get_day(match):
    return f"Ah, {match.group(1).capitalize()}! How's your week going?"

def coffee_type(kafes):
    return f"Cool!, {kafes.group(1).capitalize()} Great choice! Coffe solves everything!"

responses = [
    (re.compile(r'.*i just woke up.*', re.IGNORECASE), lambda m: "Good morning! Did you sleep well?"),
    (re.compile(r'.*Very good.*', re.IGNORECASE), lambda m: "Great to hear!"),
    (re.compile(r'.*i have no idea what to do.*', re.IGNORECASE), lambda m: "That sounds tough. Want to talk about it?"),
    (re.compile(r'.*i am bored.*', re.IGNORECASE), lambda m: "Maybe it's time to try something new!"),
    (re.compile(r'.*today is (monday|tuesday|wednesday|thursday|friday).*', re.IGNORECASE), get_day),
    (re.compile(r'.*i need coffee.*', re.IGNORECASE), lambda m: "Coffee solves everything. Espresso or cappuccino?"),
    (re.compile(r'.*(espresso|cappuccino).*', re.IGNORECASE), coffee_type),
    (re.compile(r'.*nothing makes sense.*', re.IGNORECASE), lambda m: "Sometimes things are messy. Let's try to unpack it."),
    (re.compile(r'.*i forgot my password.*', re.IGNORECASE), lambda m: "Don't worry, happens to all of us. Have you tried resetting it?"),
    (re.compile(r'.*my phone is acting weird.*', re.IGNORECASE), lambda m: "Try turning it off and on again. Classic fix."),
    (re.compile(r'.*why is everything so hard.*', re.IGNORECASE), lambda m: "You're not alone. Want to talk about what's going on?"),
    (re.compile(r'.*thank you.*', re.IGNORECASE), lambda m: "You're welcome! Anytime :)")
]

def chatbot():
    print("ELIZA: Hey! What's on your mind?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("ELIZA: Bye! Talk soon.")
            break
        matched = False
        for pattern, response in responses:
            match = pattern.match(user_input)
            if match:
                print("ELIZA:", response(match))
                matched = True
                break
        if not matched:
            print("ELIZA: Okay, cool!")


chatbot()