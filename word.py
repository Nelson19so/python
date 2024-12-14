# Title : NUMBER GUESSING GAME

import random
import time


# code 1.
# this is where the game starts, it will first pop up.
def display_menu():
    print("NELSON BRINGS YOU TO LIVE")
    print("Welcome to Number Guessing Game Puzzle! 🧠")
    print("click '1' to Select Level")
    print("click '2' to cancel")


# code 2.
# this is the second popup of the game,
# which displays and ask the user to select their level.
def game_level():
    print("Choose your game level!")
    print("click '3' for Easy mode(10 chances🛫)")
    print("click '4' for Hard mode (5 chances🛫)")


# code 4.
# this is the last popup, which is
# charge of the last and asks whether the user wants to play again or not.
def end_menu():
    print("thank you for playing................................:)")
    print("click '5' to play again 🔂")
    print("click '6' to exit")


# code 3.
# this is the main function of the game,
# it will ask the user to guess the number and hint will be given.
def play_game(chances):
    number = random.randint(1, 100)
    print("™Guess the number from range 1 to 100 ")

    chances -= 1
    if chances == 0:
        print("You lose! 😥")
        print("The number was:", number)
        try_again_menu()

    while chances > 0:
        guess_number = int(input("guess: "))
        print("")
        print("")
        if guess_number < number:
            print("wrong number ❌")
            print("Number too low! ")
            print("try again")
        elif guess_number > number:
            print("wrong number ❌")
            print("Number too high! ")
            print("try again")
        elif guess_number == number:
            print("You win! 🎉🎊🏆")
            try_again_menu()

        print("Number of chances left: ", chances)


# code 4.1.
# this is also related to end menu, this is where the engine for end menu start.
def try_again_menu():
    end_menu()
    choice = int(input("Enter your choice: "))
    print("°")
    print("•")
    if choice == 5:
        main()
    elif choice == 6:
        print("thank you for selecting your choice :)")
    else:
        print("invalid input  :(")
        try_again_menu()


# code 3.1.
# this is the main engine of the body
# for the play game, this is the main part(very very important)
def main():
    try:
        display_menu()
        choice = int(input("Enter your preference: "))
        print("°")
        print("•")
        if choice == 1:
            game_level()
            level = int(input("Enter your preferred level: "))
            if level == 3:
                play_game(10)
            elif level == 4:
                play_game(5)
            else:
                print("Wrong input")
                print("please try again")
                main()
        elif choice == 2:
            print('cancelling game......................')
            print("game cancelled!")
        else:
            print("Wrong input choice")
            print("please select again")
            main()
    except ValueError:
        print("something went wrong :(")
        print("please try again")
        main()


# code 482.4
# this is the timer of the game, it will
# start counting as soon as the user selects their level.
def timer(no):
    print("loading......")
    print("you have ", no, "s to guess the number")
    for Number in range(20, 0, -1):
        print(Number)
        time.sleep(1)
        while True:
            if Number == 0:
                print("your time has elapsed ")
                try_again_menu()
                break
            elif Number > 1:
                print("you have", Number, "seconds left.")
                #           break
                return Number
            else:
                print("you lost! 😥")


timer(20)

if __name__ == "__main__":
    main()
