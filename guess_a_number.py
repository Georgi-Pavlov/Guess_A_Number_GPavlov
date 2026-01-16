import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100):")

    if not player_input.isdigit():
        print("This is not a valid number! Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("Congratulations, you guess it!")
        break
    elif player_number > computer_number:
        print("Your number is too high!")
    elif player_number < computer_number:
        print("Your number is too low!")
