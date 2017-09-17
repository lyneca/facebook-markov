from parser import MyMessageParser
import os
import markovify
import random

names = [
    # Put Facebook first/last names here
    "Caitlin Bubb"
]
names = [x.lower() for x in names]
text_models = {}

for name in names:
    name = name.lower()
    filename = 'data/' + name.replace(' ', '_') + '.msg'
    if not os.path.exists(filename):
        open(filename, 'x').close()
        print('Extracting user messages for {}...'.format(name))
        parser = MyMessageParser(name, filename)
        parser.feed(open('messages.htm').read())

    with open(filename) as f:
        text = f.read()

    print('Generating text model for {}...'.format(name))
    text_models[name] = markovify.NewlineText(text)

def capitalize(s):
    return ' '.join([x.capitalize() for x in s.split()])

while True:
    for i in range(10):
        name = random.choice(names)
        print(capitalize(name) + ': ' + text_models[name].make_short_sentence(140))
    input()
