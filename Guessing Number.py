import random

def inputValidation(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Whoops! Please enter a valid number!")

while True:
    min = inputValidation("Pick a minimum number! ")
    max = inputValidation("Pick a maximum number! ")
    number = random.randint(min, max)
    attempts = 1

    print("Picking number... Done!")
    print("Your attempts " + str(attempts))
    guess = inputValidation("Guess my number! ")

    while guess != number:
        attempts += 1
        if guess > max:
            print("Woah there! Your number is higher than the maximum number you chose!")
            print("The maximum number is", max)

        elif guess > number:
            print("Uh oh! Your number is too high!")

        elif guess < min:
            print("Woah there! Your number is lower than the minimum number you chose!")
            print("The minimum number is", min)

        elif guess < number:
            print("Uh oh! Your number is too low!")

        else:
            print("Is that a number? I don't think so! So guess my number! ")

        print("Your attempts " + str(attempts))
        guess = inputValidation("Guess my number! ")

    print("You found it! My number is actually " + str(number) + ". Congratulation! (" + str(attempts) + " attempts)")

    while True:
        nextGame = str(input("Play Again? (Y/N) ").strip().upper())
        if nextGame in ("Y", "N"):
            break
        print("Please enter Y or N!")

    if nextGame == "N":
        break