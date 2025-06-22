import random

Difficulties = {"easy":50, "medium":100, "hard":250, "extreme":1000}


def Menu():
    while True:
        print("Difficulties: Easy, Medium, Hard, Extreme")
        Difficulty = input("Enter difficulty: ").lower()
        Range = GetRange(Difficulty)
        if Range != 0:
            RandomNumber = random.randint(0,Range)
            PlayGame = Game(RandomNumber)
            print("")
            print(f"The number was {RandomNumber}")
            print("Game Over!")
            break
        else:
            print("Not a valid difficulty! Try again.")

def Game(Number):
    Attempt = 10
    Guessed = False
    GuessedNumbers = []
    while True and Attempt > 0:
        print("")
        try:
            Guess = int(input("Enter your guess: "))
            if Guess == Number:
                print("You have guessed the number!")
                print(f"You had {Attempt} attempts left")
                break
            elif Guess  in GuessedNumbers:
                print("You already guessed that!")
                Attempt -= 1
                print(f"You have {Attempt} attempts left")
            elif Guess > Number:
                print("The number your are trying to guess is lower")
                GuessedNumbers.append(Guess)
                Attempt -= 1
                print(f"You have {Attempt} attempts left")
            elif Guess < Number:
                print("The number your are trying to guess is higher")
                GuessedNumbers.append(Guess)
                Attempt -= 1
                print(f"You have {Attempt} attempts left")
        except ValueError:
            print("Error! Try again.")
            Attempt -= 1
            print(f"You have {Attempt} attempts left")

        
    
def GetRange(Difficulty):
    if Difficulty in Difficulties:
        return Difficulties[Difficulty]
    else:
        return 0
        
Menu()