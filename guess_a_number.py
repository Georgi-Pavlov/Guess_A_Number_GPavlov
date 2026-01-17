import random

computer_number = random.randint(1, 100)

lives = 0

while True:
    difficulty = input("Select difficulty [easy / medium / hard]: ").lower()

    if difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("Invalid choice. Even this part has rules. Try again.")
    elif difficulty == "easy":
        lives = 10
        break
    elif difficulty == "medium":
        lives = 7
        break
    elif difficulty == "hard":
        lives = 5
        break

while True:
    try:
        player_input = input("Guess the number (1-100):")
        player_number = int(player_input)
        if 1 <= player_number <= 100:
            if player_number == computer_number:
                print(f"Correct!\nI am impressed. Slightly. Don’t let it get to your head.")
                break
            elif player_number > computer_number:
                lives -= 1
                if lives == 0:
                    print(
                        f"Out of lives! The number was {computer_number}. The computer feels achieved and is judging you silently.")
                    break
                print("That number has dreams bigger than reality. Try lower.")
            elif player_number < computer_number:
                lives -= 1
                if lives == 0:
                    print(
                        f"Out of lives! The number was {computer_number}. The computer feels achieved and is judging you silently.")
                    break
                print("Too low. Aim higher. I believe in you. A little.")
        else:
            lives -= 1
            if lives == 0:
                print(
                    f"Out of lives! The number was {computer_number}. The computer feels achieved and is judging you silently.")
                break
            print(f"Bold choice. Unfortunately, completely out of range.\nTry again...")
    except ValueError:
        lives -= 1
        if lives == 0:
            print(
                f"Out of lives! The number was {computer_number}. The computer feels achieved and is judging you silently.")
            break
        print(f"Interesting input. Completely useless, but interesting.\nTry again, this time with a whole number...")
