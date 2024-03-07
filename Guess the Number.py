import random;
generatedNumber = random.randrange(1,10)
userGuess = int(input('Guess a number in the range 1-10:'))
if userGuess == generatedNumber:
    print('You have got it right!')
elif userGuess < generatedNumber :
    print('Your guess is to low')
else:
    print('Your guess is too high')