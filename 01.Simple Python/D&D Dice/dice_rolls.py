import random

def dice_roll_generator(dice):
    return random.randint(1, dice)

while True:
    dice_input = input("Enter the dice roll (e.g., '2d6' or 'd20'): ")

    if dice_input.lower() == "exit":
        break

    if dice_input.startswith('d'):
        dice = int(dice_input[1:])
        throws = 1
    else:
        try:
            throws, dice = map(int, dice_input.split('d'))
        except ValueError:
            print("Invalid dice input. Continuing...")
            continue

    print(f"Rolling {throws}d{dice}:")
    for throw in range(throws):
        dice_result = dice_roll_generator(dice)
        print(f"Throw #{throw + 1}: {dice_result}")
