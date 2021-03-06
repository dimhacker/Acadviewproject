from details import spy, friends, Spy, ChatMessage

from termcolor import colored

from steganography.steganography import Steganography



Status = ["Available", "Busy", "Do not disturb"]

def ask_details():
    while True:
        spy.name = raw_input("Enter your name:")
        bool = True
        for x in spy.name:
            if x.isalpha() == False and x.isspace == False:
                bool = False

        if len(spy.name) == 0 or spy.name.isspace() == True or bool == False:  # checking name validation
            print "Hey! You haven't entered a correct name!"
        else:
            break
    spy.age=int(raw_input("Enter your age:"))
    if spy.age < 12 or spy.age > 50:
        print "You are not a spy of desired age."
        return
    spy.rating=float(raw_input("Enter the rating:"))
    spy.online=raw_input("Online(True/False):")
    print "Authentication completed!"
    print "%s %s of age %d ,rating %f is welcomed in the Ephermal Spychat App"%(spy.salutation,spy.name,spy.age,spy.rating)
    ask_choices()


def add_friend():
    spy_friend = Spy("", "", 0, 0.0, "",[])
    while True:
        spy_friend.name = raw_input("Enter name of your friend :")
        bool= True
        for x in spy_friend.name :
            if x.isalpha() == False and x.isspace() == False:
                bool=False

        if len(spy_friend.name) == 0 or spy_friend.name.isspace() == True or bool == False:  # checking name validation
            print "Hey! You haven't entered a correct name!"
        else:
            break

    spy_friend.salutation = raw_input("Should I call your friend Ms. or Mr. ?")
    if spy_friend.salutation not in ["Ms.", "MS.", "ms", "ms.", "Mr", "Mr.", "MR.", "mr", "mr."]:
        spy_friend.salutation = ""
    spy_friend.age = int(raw_input("Enter age for your friend:"))
    if spy_friend.age < 12 or spy_friend.age > 50:  # checking age validation
        print "Your friend is not of the desired age."
        return
    spy_friend.rating = float(raw_input("Enter the rating:"))
    if spy_friend.rating < spy.rating:
        print "Your friend has less rating ,can't be your friend."
        return
    spy_friend.online = raw_input("Online Status:(True/False)")
    friends.append(spy_friend)
    print "Authentication  completed!!"
    print "Now you have %d Friends!!" % len(friends)



def choose_friend():
    print "Select a friend from your friend list :"
    s_no = 0
    for friend in friends:
        print "%d.%s" % (s_no+1, friend.name)
        s_no = s_no + 1

    chat_with = int(raw_input())
    if chat_with > len(friends):
        print "No such friend exists!!"
        return None
    else:
        return (chat_with -1)


def send_message():
        chat_with   =  choose_friend()
        if chat_with != None:

            original_image = raw_input("What is the name of the image?")
            output_path = "dimple.jpg"
            text = raw_input("What do you want to say? ")
            Steganography.encode(original_image, output_path, text)

            new_chat = ChatMessage(text,len(text) ,True)

            friends[chat_with].chat.append(new_chat)

            print "Your secret message image is ready!"


def read_message():

        sender = choose_friend()

        emergency_text =["SOS","SAVE ME","HELP ME"]

        if sender != None:

            output_path = raw_input("What is the name of the file?")

            secret_text = Steganography.decode(output_path)

            if len(secret_text) ==0 or secret_text.isspace()==True:
                print "Your friend has sent a blank message!"


            else:
                if len(secret_text) <= 4 :

                    new_chat = ChatMessage(secret_text,len(secret_text), False)

                    friends[sender].chat.append(new_chat)

                    for i in emergency_text:
                        if secret_text.find(i)>-1:
                            print "Your friend %s needs your help!!"%friends[sender]
                            break
                    else:

                        print "Your secret message has been saved!"

                else:
                    print  "Your friend is talking too much,we are removing him from your friend list."
                    friends.remove(friends[sender-1])
		    	


def add_status():
    updated_status= None
    if spy.current_status==None:
        print "You have no current status!"
    else:
        print "Your current status is %s"%(spy.current_status)
    if len(Status) >0:
        choice=raw_input("Do you want to update the status from the old status(Y/N):")
        if choice.upper() =="Y":
            num=1
            for status in Status:
                print "%d.%s"%(num,status)
                num+=1
            status_no=int(raw_input("Enter the status number you want to update"))
            if status_no >len(Status):
                print "You have entered a wrong choice"
            else:
                print "Your new status is %s"%Status[status_no-1]
                updated_status=Status[status_no-1]
        elif choice.upper()=="N":
            new_status=raw_input("Enter your new status:")
            if len(new_status)>=0 and new_status.isspace() == False:
                print "Your new status is %s"%new_status
                Status.append(new_status)
                updated_status=new_status
            else:
                print "Invalid status"


    return updated_status



def read_chat_history():
    friend=choose_friend()
    if friend!= None:
            for Chat in friends[friend].chat:
                if Chat.sent_by_me:
                    print colored('[%s] ' % (Chat.time.strftime("%d %B %Y")),"blue") ,colored('You said:',"green")
                    print "%s"%Chat.message

                else:
                    print colored ('[%s] ' % (Chat.time.strftime("%d %B %Y")),"blue") ,colored("%s said :"%friends[friend].name,"green")
                    print "%s" %Chat.message


def ask_choices():
    while True:
        choice = int(raw_input("Enter 1.To add a friend\n2.To send a message \n3.To read a message\n4.To update status\n5.To read chat history\n6.To exit the application\n"))
        if choice == 1:
            add_friend()
        elif choice == 2:
            send_message()
        elif choice == 3:
            read_message()
        elif choice == 4:
            spy.current_status=add_status()
        elif choice== 5:
            read_chat_history()
        elif choice == 6:
            print "BYE see you soon!!"
            exit()

old_spy=True
print "Do you want to continue as %s:(Y/N)?" % spy.name
option = raw_input()
if option.upper() == "Y":
    print "%s %s of age %d ,rating %f is welcomed in the Ephemeral Spychat App" % (spy.salutation, spy.name, spy.age, spy.rating)
    ask_choices()


elif option.upper() == "N":
    ask_details()


