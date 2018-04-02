#print ("Hello Default user !")

#spy = raw_input("what is your spy name:? ")
#salutation = raw_input("What should we call you Mr or Ms ?")
#spyname = salutation +" "+spy
#print ("Alright "+ spyname +" I'd like to know little bit more about you")



#spy_name = 'Ujjwal Sharma'
#spy_rating = 3.9
#spy_age = 24
#spy_salutation = 'Mr'

####### Information Of A Default User #######
from datetime import datetime

# default status
current_status_message = None

# list of default status
status = ['My name is ujjwal.', 'Location: New Delhi']


class User:
    # create class
    def __init__(self, uname, salutation, age, rating):
        self.uname = uname
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# define user_name, age, rating
user_1 = User('Mr. ujjwal', 20, 3.8)
user_2 = User('Mr. Ujjwal', 21, 2.6)

# details of some existing friends
friend_one = User('vivek', 'Mr.', 24, 4.5)
friend_two = User('Jay', 'Ms.', 28, 3.1)
friend_three = User('Shivam', 'Mr.', 26, 3.6)

# lists of friends
friends = [friend_one, friend_two, friend_three]