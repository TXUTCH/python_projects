import random

answerList = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}
rules = { "r": "s", "p": "r", "s": "p" }

wins = 0
losses = 0
draws = 0

while True:
    answer = input("(R)ock, (P)aper, or (S)cissors? ").lower()

    if answer not in rules:
        print("Bruh, pick a valid answer!")
        continue

    botAnswer = random.choice(["r", "p", "s"])

    print("Rock, Paper, Scissors!")

    print(f"Bot chose: {answerList[botAnswer]}")
    print(f"You chose: {answerList[answer]}")
    if answer == botAnswer:
        print("It is a draw!")
        draws += 1
    elif rules[answer] == botAnswer:
        print("You won this round!")
        wins += 1
    elif rules[answer] != botAnswer:
        print("You lost this round!")
        losses += 1

    print(f"Your score -> Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print("-" * 30)

    while True:
        nextGame = str(input("Play Again? (Y/N) ").strip().upper())
        if nextGame in ("Y", "N"):
            break
        print("Please enter Y or N!")

    if nextGame == "N":
        print(f"Final score -> Wins: {wins}, Losses: {losses}, Draws: {draws}")
        print("Thanks for playing!")
        break
