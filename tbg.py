import random

def roomGen():
    num = random.randrange(0,100)
    if num < 25:
        return 2
    elif num < 50:
        return 3
    elif num < 75:
        return 4
    elif num < 100:
        return 5
    

def roomescription(num):
    if num == 2:
        print ("You are in a crew cabin. You see several bunk beds on both sides of the room, neatly made with tighly tucked-in wool blankets. A folding table with several chairs sits in the middle of the room, covered with cards, empty cups, and bubblegum wrappers. It appears that nobody has been in this room for quite some time.")
    elif num == 3:
        print ("You are in the Engine room")
    elif num == 4:
        print ("You are in the Storage room")
    elif num == 5:
        print ("You are in the kitchen")
        
        
user = input(" Do you want to go into the rooms")
if user == 'yes':
    if roomGen() == 2:
        roomescription(2)
    if roomGen() == 3:
        roomescription(3)
    if roomGen() == 4:
        roomescription(4)
    if roomGen() == 5:
        roomescription(5)
        
