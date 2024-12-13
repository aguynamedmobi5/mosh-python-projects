import random

dice_rolling_counter = 0


def randomDiceValues():
    return random.randint(1, 6)


def die_thrower(count):
    num_list = []
    for i in range(count):
        num_list.append(randomDiceValues())
    return tuple(num_list)


while True:
    user_input = input("Roll the dice? (y/n): ").lower()

    if user_input == "y":
        dice_rolling_counter += 1
        try:
            num_of_dice = int(input("Enter the number of dice you want to roll: "))
            print(die_thrower(num_of_dice))
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elif user_input == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice!")

print(f"You have rolled the dice {dice_rolling_counter} times")