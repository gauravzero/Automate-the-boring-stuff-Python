# Ask for the name
# Well Name, Im thinking of a number between 1 and 20
# Take a Guess
# 6 guesses to get it right
# If guessed correctly, tell them
# the number of guesses it took too

import random

print('Hi, Whats your name?')
name = input()
print('Hi ' + name + ', lets play a game. I\'ll choose a number between' 
      '0 and 20(including both), and you got to guess it')

answer = random.randint(0,20)
guesses = 0
while(guesses < 6):
    guesses = guesses + 1
    print('Take a Guess')
    userGuess = input()
    intUserGuess = int(userGuess)
    if intUserGuess == answer:
        print('Thats right! You got it in '+ str(guesses) + ' times!')
        break
    elif intUserGuess < answer:
        print('Its higher')
    elif intUserGuess > answer:
        print('Its lower')
if guesses == 6 :
    print('Whoops, you took too many guesses! The number was ' + str(answer))
else :
    print('Good Job, Bye!')