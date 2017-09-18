from message_parser import MessageSaver

print("Saving...")
parser = MessageSaver()
parser.feed(open('messages.htm').read())
