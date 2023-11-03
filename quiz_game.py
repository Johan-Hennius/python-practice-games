print("Welcome to my quiz")

total_score = 0
playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Let's play.")

answer = input("What genus does the Penny Bun mushroom belong to? ")
if answer.lower() == "boletus":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect.")

answer = input("What genus does the Meadow Waxcap mushroom belond to? ")
if answer.lower() == "hygrocybe":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect!")

answer = input("What genus does the Chanterelle mushroom belond to? ")
if answer.lower() == "cantharellus":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect!")

answer = input("What genus does the Grey Oyster mushroom belond to? ")
if answer.lower() == "pleurotus":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect!")

answer = input("What genus does the Chicken of the woods mushroom belond to? ")
if answer.lower() == "laetiporus":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect!")

answer = input("Final question: What is the best pancake topping? ")
if answer.lower() == "cream and jam":
    print("Correct!")
    total_score += 1
else:
    print("Incorrect!")

print(f"Game over.\nTotal Score: {total_score}")