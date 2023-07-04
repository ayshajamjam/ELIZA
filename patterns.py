patterns = {
    r'.*(hi|hola|i\'m back|hello|good morning|good afternoon).*': [
        "Hello, how are you feeling today?",
        "How do you do? Please tell me your problem",
        "What's going on?"
    ],
    r'.*(quit|pause|exit|goodbye|bye|later|good night|cya).*': [
        "Goodbye",
        "Till next time",
        "Hope to see you again soon",
        "Come back and chat soon!",
        "Alright, talk soon"
    ],
    r'.*(yes|certainly|yup).*': [
        "You seem quite positive",
        "You are sure",
        "I see",
        "I understand"
    ],
    r'.*(perhaps|maybe|I think).*': [
        "You don't seem quite certain",
        "Why the uncertain tone?",
        "Can't you be more positive?",
        "You aren't sure...",
        "Don't you know?"
    ],
    r'.*(dream|dreams).*': [
        "What does that dream suggest to you?",
        "Do you dream often?",
        "What people appear in your dreams?",
        "Don't you believe that dream has something to do with your problem?"
    ],
    r'.*I?\w?(want|need|would like) (.*)': [
        "Why do you want {0}?",
        "What would you do if you got {0}?",
        "Are you sure you need {0}?"
    ],
    r'.*I?\w?feel (.*)': [
        "Why do you feel {0}?",
        "Can you explain why you feel {0}?",
        "Do you often feel {0}?"
    ],
    r'.*I?\w?(love|hate) (.*)': [
        "Why do you {0} {1}?",
        "What makes you {0} {1}?",
        "How does it feel to {0} {1}?"
    ],
    r'.*\w?(everyone|everybody|nobody|noone)\w?.*': [
        "Really, {1}",
        "Surely not {1}",
        "Can you think of anyone in particular?",
        "Who, for example?",
        "You are thinking of a very special person",
        "Who, may I ask?",
        "Some special perhaps",
        "You have a particular person in mind, don't you?",
        "Who do you think you're talking about?"
    ],
    r'.*\w?(today|now)\w?.*': [
        "Really, {1}",
        "When else?",
        "I see"
    ],
    r'.*\w?(tomorrow|next week|next month|next year)\w?.*': [
        "Really, {1}",
        "When else?",
        "I see"
    ],
    r'.*\w?(yesterday|previously|before|last week|last month|last year)\w?.*': [
        "Really, {1}",
        "When else?",
        "Did it happen before that",
        "I see"
    ],
    r'.*\w?(sad|upset|bored|confused|tired|unhappy|scared|concerned|lost|belittled|weak|frustrated|small)\w?.*': [
        "Really, {1}",
        "Do you often feel {1}",
        "Why do you think you are {1}",
        "What do you do when you feel {1}",
        "When in particular?",
        "In what circumstances?",
        "You are thinking of a very special person"
    ],
    r'.*\w?always\w?.*': [
        "Can you think of a specific example?",
        "When?",
        "What incident are you thinking of?",
        "Really, always?"
    ],
    r'.*\w?because\w?.*': [
        "Is that the real reason?",
        "Don't any other reasons come to mind?",
        "Does that reason seem to explain anything else?",
        "What other reasons might there be?"
    ],
    r'.*': [
        "Please go on.",
        "Tell me more.",
        "I see.",
        "How does that make you feel?",
        "I am not sure I understand you fully",
        "What does that suggest to you?"
    ]
}