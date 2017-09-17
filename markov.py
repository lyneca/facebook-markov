from parser import MyMessageParser
import markovify
import os

if __name__ == '__main__':
    # Put Facebook first/last names here
    names = [
    ]
    for name in names:
        name = input("Name: ").lower()
        filename = name.replace(' ', '_') + '.msg'
        if not os.path.exists(filename):
            open(filename, 'x').close()
            print('Extracting user messages...')
            parser = MyMessageParser(name, filename)
            parser.feed(open('messages.htm').read())
'''

    with open(filename) as f:
        text = f.read()

    print('Generating text model...')
    text_model = markovify.NewlineText(text)
    print('Done. Press enter to generate sentences.')
    while True:
        print(text_model.make_sentence())
        input()


'''
