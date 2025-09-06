import random
import string

length = int(input("Enter password length (chars, min 4): "))
totalPw = int(input("How many passwords? "))

for total in range(totalPw):
    characters = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    if length >= 4:
        all_chars = string.ascii_letters + string.digits + string.punctuation
        characters += random.choices(all_chars, k=length - 4)
    else:
        print("The minimum is 4!")
        exit()
    random.shuffle(characters)
    password = "".join(characters)
    print(f"Password {total+1} is:", password)
    print("-" * 30)
