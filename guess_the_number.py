import random

print("Find the number that I have in my mind")

secret = random.randint(1, 100)

while True:
    print("Guess the number")
    guess = int(input())
    if guess > secret:
        print("Your number is too big. Try small vale")
    elif guess < secret:
        print("Your number is too small. Try higher value")
    else:
        print("Your guessed right: ", guess)
        break

