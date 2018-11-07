import MailClient from MailClient
import MailServer from MailServer

class MailItem:
    def __init__(self, sender, receiver, msg):
        self.sender = sender
        self.receiver = receiver
        self.msg = msg
    
    def print(self):
        print("From: " + self.sender)
        print("To: " + self.receiver)
        print("Message: " + self.msg)





