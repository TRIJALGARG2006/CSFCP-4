import random


secret_number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")

while True: 
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("You won! Good job.")
        break  
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")