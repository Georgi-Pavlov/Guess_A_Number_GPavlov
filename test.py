import random

computer_number = random.randint(1, 5)

while True:
    try:
        player_number = input()
        if 1 <= int(player_number) <= 5:
            if int(player_number) == computer_number:
                print("Congratulations, you guessed it!")
                break
        else:
            print("Number is out of range! Try again...")
    except ValueError:
        print("Please write a whole number within the specified range. Trying to negotiate will not work here!")

print(player_number)
