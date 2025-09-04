import random

# Difficulty levels mapped to their maximum random number
difficulties = {"easy": 50, "medium": 100, "hard": 250, "extreme": 1000}


# Main menu function that handles difficulty selection
def menu():
    while True:
        print("Difficulties: Easy, Medium, Hard, Extreme")
        difficulty = input("Enter difficulty: ").lower()
        number_range = get_range(difficulty)

        # Check if valid difficulty was entered
        if number_range != 0:
            random_number = random.randint(0, number_range)
            play_game(random_number)
            print("")
            print(f"The number was {random_number}")
            print("Game Over!")
            break
        else:
            print("Not a valid difficulty! Try again.")


# Game logic where the user tries to guess the number
def play_game(secret_number):
    attempts = 10
    guessed_numbers = []

    while attempts > 0:
        print("")
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("You have guessed the number!")
                print(f"You had {attempts} attempts left")
                break

            elif guess in guessed_numbers:
                print("You already guessed that!")
                attempts -= 1
                print(f"You have {attempts} attempts left")

            elif guess > secret_number:
                print("The number you are trying to guess is lower")
                guessed_numbers.append(guess)
                attempts -= 1
                print(f"You have {attempts} attempts left")

            elif guess < secret_number:
                print("The number you are trying to guess is higher")
                guessed_numbers.append(guess)
                attempts -= 1
                print(f"You have {attempts} attempts left")

        except ValueError:
            # Handle non-integer input
            print("Error! Please enter a valid number.")
            attempts -= 1
            print(f"You have {attempts} attempts left")


# Helper function to get the range based on difficulty
def get_range(difficulty):
    if difficulty in difficulties:
        return difficulties[difficulty]
    else:
        return 0


# Program entry point
if __name__ == "__main__":
    menu()
