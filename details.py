from datetime import datetime
class Spy:
    def __init__(self, name, salutation, age, rating, online, chat):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = online
        self.chat=[]
        self.current_status=None


class ChatMessage:

    def __init__(self,message, message_length, sent_by_me):
        self.message = message
        self.message_length=message_length
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy("Dimple", "Ms.", 20, 5.0, True, [])
friend1=Spy("John", "Mr.", 23, 6.8, True, [])
friend2=Spy("Neil", "Mr.", 22, 6.0, True, [])
friends = [friend1, friend2]
