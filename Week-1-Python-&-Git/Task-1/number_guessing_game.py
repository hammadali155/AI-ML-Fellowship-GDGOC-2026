import random
target = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))
if guess == target:
    print("Correct!")
else:
    print(f"Wrong, it was {target}")