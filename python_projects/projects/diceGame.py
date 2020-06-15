import random

possibleAnswers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
userScore = 0
userTries = 7
print("Welcome to the dice game! where you guess the number thats about to be rolled. Get a score of 3 to win!")
print("Your score is:", userScore, "\n")
 
while True:
    diceTuple = (1, 2, 3, 4, 5, 6) #make dice Tuple a tuple data inside the tuple will never change
    diceNum = random.choice(diceTuple) + random.choice(diceTuple) # setting the variable diceNum to random choice and add the 2 choices together
    print("Tries left:", userTries, "\n")
    userGuess = int(input("Enter your guess: " )) # setting the user guess to a int instead of a string
    if(userGuess not in possibleAnswers): # checks if the guess is in the possible answer tuple
        print(userGuess, "\nis not a valid guess, try again.")
        userTries -= 1
    else: # if the user guess is in the possible answers tuple continue to the next block of code
        print("\nThe dice rolled...", diceNum)
    if(diceNum == userGuess): # checks if the users guess is =  to the random dice roll then adds +1 to score
        userScore += 1
        print("You guessed it right! +1")
        print("Your score:", userScore)
    elif(diceNum != userGuess): #if random dice roll doesnt = user guess -1 try
        userTries -= 1
        print("You guessed wrong try again -1 try")
        print("Your score: ", userScore)
    if(userScore == 3): #when user reaches a score of 3 break out of the loop
        break
    if(userTries == 0): #when the user hits 0 tries break out of the loop
        break
 
