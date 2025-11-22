import random
a = int(input("enter a number:"))
secret_number = random.randint(1, a)

print(f"I am thinking of a number between 1 and {a}.")

while True: 
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("You won! Good job.")
        break  
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")