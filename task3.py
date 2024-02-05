import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(1)
    print("Do you want to enter the cave? (yes/no)")

def make_choice():
    while True:
        choice = input("> ").lower()

        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def explore_cave():
    print("\nYou enter the dark cave and start exploring.")
    time.sleep(1.5)
    print("As you walk deeper, you see two paths. One on the left and one on the right.")
    time.sleep(1.5)
    print("Which path do you choose? (left/right)")

    choice = input("> ").lower()

    if choice == 'left':
        print("\nYou encounter a friendly creature. It gives you a treasure!")
    elif choice == 'right':
        print("\nYou find a hidden passage that leads to an underground river.")
        time.sleep(1.5)
        print("Do you want to swim across the river? (yes/no)")

        if make_choice():
            print("\nYou successfully swim across the river.")
        else:
            print("\nYou decide not to risk it and find another way back.")

    time.sleep(1)
    print("\nYou continue your adventure...")
    # You can extend the story with more choices and outcomes.

def main():
    introduction()

    if make_choice():
        explore_cave()
    else:
        print("\nYou choose not to enter the cave. The adventure ends.")

if __name__ == "__main__":
    main()
