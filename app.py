from flask import Flask, render_template, request
import re
import random
from patterns import patterns

app = Flask(__name__)
hello_commands = ('hi', 'hola', 'i\'m back', 'hello', 'good morning', 'good afternoon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
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
    else:
        response = "ELIZA: Can you frame that in another way for me?"

    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
