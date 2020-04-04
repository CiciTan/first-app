# This is our first trial program
# By Tony

import random


# random is a module.
# A module in Python include functions, constants, classes (with fields and methods encapsulated inside)
# First import the module first.
# To call the function, unfortunately you have to include the module name before the function. For example:
# 	random.seed()
# To reduce the hustle during writing, you could instead import the function you want. For example:
# 	from random import seed
# Now you can directly call the seed function:
# 	seed()

# Verify whether the player wants to continue. Filter out invalid responses.
# Return True or False only
def validate_continue() -> bool:
    while True:
        ans = input("Do you want to continue? Y/N \n")
        if (ans == 'n') or (ans == 'N') or (ans == "no") or (ans == "No") or (ans == "NO") or (ans == "Nope") or (
                ans == "nope"):
            return False
        elif (ans == 'y') or (ans == 'Y') or (ans == "yes") or (ans == "Yes") or (ans == "YES") or (ans == "Yeah") or (
                ans == "yeah"):
            return True
        else:
            print("Answer not valid! Please try again.")

# Convert user input into int. Filter out invalid input.
# Return int
def input_num() -> int:
    while True:
        try:
            keyin = int(input("Please guess an integer between 0 to 3: \n"))
            return keyin

        except ValueError:
            print("Invalid input! Please try again.")


# Generate a random integer
# Return int
def gen_random_int() -> int:
    random.seed()
    # Seed is required to generate random numbers
    return int(random.random() * 3)


# random.random() generates a random number between 0 to 1

# Game logic, validate whether user guessed correctly
# No return
def win_or_lose(random_int, input_num):
    if random_int == input_num:
        print("Yeah, you guessed right!")
    else:
        print("Nope, wrong guess. My number is actually: ", random_int)


# Main thread is here
while True:

    win_or_lose(gen_random_int(), input_num())

    if not validate_continue():
        break

print("Thanks for playing")
