import random
a = (random.randint(0,9))
playing = True
print("Hello  I'm Easy Number Guesing.\n I will generate a number from 0 to 9,\n and you have to guess the number one digit at a time.")
while playing:
    guess = int(input("Please enter your guess:  "))
    if guess == a:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, that's not the correct number Try again ")
        if guess < a:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")