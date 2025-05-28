import random

top_range = input("type a number: ")

if top_range.isdigit:
    top_range = int(top_range)

    if top_range <= 0:
        print("PLease enter a number that is bigger than 0")
else: 
    print("Please type a number next time")
    quit()

number = random.randint(0, top_range)
num_of_guess = 0
guess_count = 0

while guess_count < 5:
    num_of_guess += 1
    guess_count += 1

    guess = int(input("guess the number: "))
    if guess == number:
        print(f"Correct!! You guessed this right on {num_of_guess} tries")
        quit()
    else:
        print("wrong")
print(f"Thanks for playing, the number is: {number}")