import random

computer_number = random.randint(1, 100)

while True:
    try:
        player_input = input("Guess the number (1-100):")
        player_number = int(player_input)
        if 1 <= player_number <= 100:
            if player_number == computer_number:
                print("Congratulations, you guessed it!")
                break
            elif player_number > computer_number:
                print("Your number is too high!")
            elif player_number < computer_number:
                print("Your number is too low!")
        else:
            print("Number is out of range! Try again...")
    except ValueError:
        print("Please write a whole number within the specified range. Trying to negotiate will not work here!")
