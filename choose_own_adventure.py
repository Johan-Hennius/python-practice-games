name = input("Type your name: ")
print(f"Welcome {name} to adventure")

answer = input("You are walking through the woods. You see a fork in the road ahead of you and you can go left or right. \nWhich way do you go? (left or right) ")

if answer.lower() == "left":
    answer_2 = input("You come to a hut made of sweets. \nDo you knock or carry on? (knock or carry on)")

    if answer_2.lower() == "knock":
        
        answer_3 = input("An old lady answers the door and offers for you to come in for food. \nDo you enter or scream? (enter or scream)")
        if answer_3.lower() == "enter":
            input()
        elif answer_3.lower() == "scream":
            input()  
        else:
            print("Game Over")
        
    elif answer_2.lower() == "carry on":
        print()
    else: 
        print("Game Over")

elif answer.lower() == "right":
    print()
else:
    print("Game Over")