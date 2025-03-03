# Given a positive integer x. Your task is to check, if it is even or odd

while True:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Number invalid")
        break
    elif number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


