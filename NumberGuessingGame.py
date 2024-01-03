# random module is used to generate random numbers
import random

random_number = random.randint(1, 20)
# Adding the players previous guesses to a list
list_of_guesses = []
# print(random_number)
# Prompting the player to guess the number
while True:
    try:
        guess = int(input("Guess the number between 1 and 20: "))
        list_of_guesses.append(guess)
        # check if the guess is correct
        if guess == random_number:
            print("Yaay! You guessed right.")
            break
        elif guess > random_number:
            print("Too high")
            break
        elif guess < random_number:
            print("Too low")
        else:
            print("OH NO! Better luck next time.")
    except ValueError:
        print("Thats not a number! Please enter a valid integer.")


print("You guessed the following number: ", list_of_guesses)

random_number()
