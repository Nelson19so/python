# World guessing game

import random as random
import time as time


# this will first display at the start of the game
def menu():
    print("welcome to word guessing game")
    print("click '1' to play game ")
    print("click '2' to exit from game ")


# this will display st the level of the game
def game_level():
    print("click '3' for 10 chances ")
    print("click '4' for 7 chances ")
    print("click '5' for 5 chances  ")


def play_game(chances, win, lost):
    win += 1
    lost -= 1
1
    words = ['rock', 'paper', 'scissors']
    word = random.choice(words)
    #    print("computer has chosen", word)
    print("loading game•...........")
    while chances > 0:
        guess = input(" AI:) ROCK, PAPER, SCISSORS?: ")
        print("")
        print("")
        if guess == 'rock' and word == 'scissors':
            print("you win")
            print("congratulations!")
            print("you win", win, "times")
            print("computer lost -1 point. point remaining:", lost)
            print("computer chose", word, "and you chose", guess)
            break
        elif guess == 'paper' and word == 'rock':
            print("you win")
            print("congratulations!")
            print("you win", win, "times")
            print("computer lost -1 point. point remaining:", lost)
            print("computer chose", word, "you chose", guess)
        elif (guess == 'rock' and word == 'rock') or \
                (guess == 'paper' and word == 'paper') or \
                (guess == 'scissors' and word == 'scissors'):
            print("try again")
            print("you chose", guess, "and computer chose", word)
        else:
            print("you lost")
            print("computer win", win, "times")
            print("you lost -1 point. point remaining:", lost)
            print("computer chose", word, "you chose", guess)
            break
    while win == 5:
        print("game finished")
        break

    while lost == 5:
        print("game over")
        break

    chances -= 1
    while chances == 0:
        print(" ")
        print("chances have finished")
        print("thank you for playing........")
        break
    if chances > 0:
        print("you have", chances, "chances left")
        play_game(chances, win, lost)
    else:
        print("you dont have any chances left")


def main():
    while True:
        try:
            menu()
            choice = int(input("Enter your choice: "))
            print("")
            print("")
            if choice == 1:
                second_main()
                break
            elif choice == 2:
                print("exiting game......")
                print("thank you for selecting your choice")
                break
            else:
                print("something went wrong")
                break
        except ValueError:
            print("something went wrong")
            main()


def second_main():
    while True:
        try:
            game_level()
            choice_2 = input("Enter your level: ")
            print("^")
            print("^")
            if choice_2 == "3":
                print("you have 10 chances")
                play_game(10, 0, 5)
                break
            elif choice_2 == "4":
                print("you have 7 chances")
                play_game(7, 0, 5)
                break
            elif choice_2 == "5":
                print("you have 5 chances")
                play_game(5, 0, 5)
                break
            else:
                print("invalid choice, try again")
                second_main()
                break
        except ValueError:
            print("something went wrong")
            second_main()

for i in range(20, -1, -1):
    print(i)
    time.sleep(0.9)
print("hello")

if __name__ == "__main__":
    main()

