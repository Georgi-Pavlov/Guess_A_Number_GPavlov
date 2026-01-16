import random

computer_number = random.randint(1, 100)

while True:
    try:
        player_input = input("Guess the number (1-100):")
        player_number = int(player_input)
        if 1 <= player_number <= 100:
            if player_number == computer_number:
                print(f"Correct!\nI am impressed. Slightly. Don’t let it get to your head.")
                break
            elif player_number > computer_number:
                print("That number has dreams bigger than reality. Try lower.")
            elif player_number < computer_number:
                print("Too low. Aim higher. I believe in you. A little.")
        else:
            print(f"Bold choice. Unfortunately, completely out of range.\nTry again...")
    except ValueError:
        print(f"Interesting input. Completely useless, but interesting.\nTry again, this time with a whole number...")
