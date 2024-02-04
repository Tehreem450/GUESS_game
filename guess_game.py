import random
randNumber=random.randint(1,100)

userGuess=0
guesses=0

while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess:"))
    guesses+=1
    if (userGuess==randNumber):
        print("you guessed it right")
    else:
        if (userGuess>randNumber):
           print("You guessed it wrong.Enter a smaller number")
        else:
            print("You guessed it wrong.Enter a larger number")
    
print(f"you guess the number in {guesses} guesses")
print (f"The random number was {randNumber}.")