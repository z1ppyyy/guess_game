'''
1.  import random
    import logo

2. print logo + greet text

# DON'T FORGET ABOUT TEST(show the card so that was easier to check) IN MY CODE

3. ask user for difficulty in game:
if easy - 10 attempts
if hard - 5 attempts

4. Make a guess:

if user's choice lower than the number - say too low
if user's choice higher than the number - say too high
if a user guessed say - You got it! The answer was {print the number}

during user's guess write him that he has 1 less attempt + Guess again + too low or too high

'''

from logo_guess import logo
import random


random_number = random.randint(1,100)
attempt = 0

print(logo)
print(

    "Welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100.\n"
    f"Pssst, the correct answer is {random_number}"
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

while attempt >0:
    if int(user_guess) < random_number:
        print("Too low")
        print("Guess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
    elif int(user_guess) > random_number:
        print("Too high")
        print("Guess again.")
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
    elif int(user_guess) == random_number:
        print(f"You got it! The answer was {random_number}")
        break
    else:
        print("Opps...")


