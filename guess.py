from logo_guess import logo
import random

random_number = random.randint(1,100)
attempt = 0

print(logo)
print(

    "Welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100.\n"
  # CODE TEST f"Pssst, the correct answer is {random_number}"
)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempt += 10
elif difficulty == "hard":
    attempt += 5
else:
    print("You chose wrong difficulty")
    exit()

print(f"You have {attempt} attempts remaining to guess the number.")

user_guess = input("Make a guess: ")

while attempt >1:
    if int(user_guess) < random_number:
        print("Too low")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
    elif int(user_guess) > random_number:
        print("Too high")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
    elif int(user_guess) == random_number:
        print(f"You got it! The answer was {random_number}")
        exit()

print("You've run out of guesses, you lose.")

