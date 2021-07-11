# Setup
opt = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, HaCKaToOnEr ?\n")
print("Welcome  to Toonslate island  , " + name + "  Let us go on a Minecraft quest!")
print("You find yourself in front of a abandoned mineshaft.")
print("Can you find your way to explore the shaft and find the treasure chest ?\n")
 
# Start of game
response = ""
while response not in opt:
    response = input("Would you like to go inside the Mineshaft?\nyes/no\n")
    if response == "yes":
        print("You head into the Mineshaft. You hear grumbling sound of zombies,hissing sound of spidersand rattling of skeletons.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a skeleton  with a golden armor and a bow  .")
    print("To your right, there is a way to go more inside the shaft.")
    print("There is a cobble stone wall directly in front of you.")
    print("Behind you is the mineshaft exit.\n")
    response = input("What direction would you like to move?\nleft/right/forward/backward\n")
    if response == "left":
        print(name+" was shot by an arrow. Farewell :( ")
        quit()
    elif response == "right":
        print("You head deeper into the mineshaft and find the treasure chest ,Kudos!!!.\n")
    elif response == "forward":
        print("You broke the stone walls and find out it was a spider spawner, spiders slain you to deeath\n")
        response = "" 
    elif response == "backward":
        print("You leave the mineshaft un explored . Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
