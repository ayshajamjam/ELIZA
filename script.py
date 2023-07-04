import re
import random
from patterns import patterns

class Eliza:

    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    def __init__(self):
        self.user_name = ""

    def welcome(self):
        self.user_name = input("ELIZA: Hello, what is your name?\nUSER: ")
        user_input = input(f"ELIZA: Okay {self.user_name}, what's going on?\nUSER: ")

        self.handle_conversation(user_input)

    def handle_conversation(self, user_input):
        while not self.exit_convo(user_input):
            user_input = self.match_reply(user_input)

    def exit_convo(self, user_input):
        for command in self.exit_commands:
            if command in user_input:
                print("ELIZA: Hope to speak again soon.")
                return True
        return False

    def match_reply(self, user_input):
        matched_pattern = None
        response = ""

        for pattern, responses in patterns.items():
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                matched_pattern = pattern
                response = random.choice(responses)
                break

        if matched_pattern:
            groups = match.groups()
            if len(groups) > 0:
                response = response.format(*groups)
            return input(f"ELIZA: {response} \nUSER: ")
        else:
            return input("ELIZA: Can you frame that in another way for me?")


Conversation = Eliza()
Conversation.welcome()