import random

def inputValidation(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Whoops! Please enter a valid number!")

totalRolls = 0
totalHighest = 0
totalLowest = 7
sumTotalRolls = 0

while True:
    highest = 0
    lowest = 7
    sumRolls = 0

    numDice = inputValidation("How many dice do you want to roll? ")
    for i in range(numDice):
        diceRoll = random.randint(1, 6)
        print(f"Dice {i+1}: {diceRoll}")
        totalRolls += 1
        sumRolls += diceRoll
        sumTotalRolls += diceRoll

        if highest < diceRoll:
            highest = diceRoll
        if lowest > diceRoll:
            lowest = diceRoll
        if totalHighest < diceRoll:
            totalHighest = diceRoll
        if totalLowest > diceRoll:
            totalLowest = diceRoll
    print(f"Total Numbers: {sumRolls}, Highest: {highest}, lowest: {lowest}")
    print("-" * 30)

    while True:
        nextRoll = str(input("Roll Again? (Y/N) ").strip().upper())
        if nextRoll in ("Y", "N"):
            break
        print("Please enter Y or N!")

    if nextRoll == "N":
        print(f"Total Rolls: {totalRolls}, Total Highest: {totalHighest}, Total Lowest: {totalLowest}")
        print(f"Total numbers: {sumTotalRolls}, Average roll: {round(sumTotalRolls / totalRolls)}")
        #print(f"You rolled: {numDice} 🎲")
        print("Thanks for playing!")
        break