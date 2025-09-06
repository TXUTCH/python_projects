count = int(input("Give me number "))
text = str(input("Give me text "))
count1 = int(input("How long? "))

value = 1
while value <= count1:
    i = 1
    while i <= count:
        print(" " * i + text)
        i += 1
    while i >= 1:
        print(" " * i + text)
        i -= 1
    value += 1