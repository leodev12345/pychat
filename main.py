import os
import sys
print("What do you want to do? \n1-create a new chat room\n2-join a chat room\n3-help")
choise=int(input("Enter your choise: "))
if choise==1:
    print("\n")
    import server
elif choise==2:
    print("\n")
    import client
elif choise==3:
    print("\n1.Creating a chat room\n\nselect 1 from the choise and share the hostname wiht your firends so they can connect to the chat room and start sending messages\n\n2.Connecting to chatroom\n\njust paste the hostname of the chatroom to enter it and start talking")
    print("\n")
    print("-----------------------")
    print("\nWhat do you want to do? \n1-create a new chat room\n2-join a chat room")
    choise=int(input("Enter your choise: "))
    if choise==1:
        print("\n")
        import server
    elif choise==2:
        print("\n")
        import client
else:
    print("Invalid input!")
