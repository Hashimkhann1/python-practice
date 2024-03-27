import random


userInput = input("Enter snake , water or gun to play the game: ")

optionList = ["snake" , "water" , "gun"]
randomOption = random.randint(0,2)

if (userInput == 'snake' or userInput == 'water' or userInput == 'gun'):
    print('you: ' + userInput)
    print('computer: ' + optionList[randomOption])

    if (optionList[randomOption] == userInput):
        print("Try again game is draw")
    elif (userInput == 'gun' and optionList[randomOption] == 'snake'):
        print("You Win the game")
    elif (userInput == 'water' and optionList[randomOption] == 'gun'):
        print("You Win the game")
    elif (userInput == 'snake' and optionList[randomOption] == 'water'):
        print("You Win the game")
    else:
        print("I win the game and you lose")
else:
    print("Enter correct option")
