from message_parser import BaseMessageParser

class MyMessageParser(BaseMessageParser):
    def __init__(self, name, filename):
        super().__init__()
        self.name = name.lower()
        self.filename = filename

    def handle_timestamp(self, timestamp):
        pass

    def handle_message(self, message):
        if self.is_user:
            with open(self.filename, 'a') as f:
                f.write(message + '\n')

    def handle_sender(self, sender):
        if sender.lower() == self.name:
            self.is_user = True
        else:
            self.is_user = False

    def handle_users(self, users):
        pass
    
