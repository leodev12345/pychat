print("What do you want to do? \n1-create a new chat room\n2-join a chat room")
choise=int(input("Enter your choise: "))
if choise==1:
    print("\n")
    import server
elif choise==2:
    print("\n")
    import client
else:
    print("Invalid input!")
