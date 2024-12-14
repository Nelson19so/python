#This code is for running ussd code on the terminal


def main_menu():
    while True:
        try:
            print("MENU")
            print("Welcome to lint ussd code")
            print("")
            print("select '1' to access data bundle")
            print("select '2' for always on")
            print("select '3' to buy for a friend")
            print("select '4' to see data balance")
            print("select '5' to exit program")
            data_bundle()
            break
        except ValueError:
            print("Please enter a valid number")
            break


def data_bundle():
    while True:
        try:
            input_ussd = int(input('Select choice: '))

            if input_ussd == 1:
                print("DATA BUNDLE")
                print("")
                print("")
                print("click '1' to buy daily data plan")
                print("click '2' to buy monthly data plan")
                print("click '3' to buy 6month's plan")
                print("click '4' to buy yearly balance")
                print("click '5' ")
                print("click '5' to exit menu")
                break
            else:
                print('Wrong input')
        except ValueError:
            print("Please enter a valid number")


def first_pop_up():
    while True:
        try:
            ussd_code = 312
            ussd_input = int(input("ussd code: "))
            if ussd_input == ussd_code:
                print("code running...")
                main_menu()
                break
            elif ussd_input > ussd_code:
                print("invalid ussd code")
                break
            else:
                print("invalid ussd code")
                break
        except ValueError:
            print("Please enter a valid number")
            break


first_pop_up()
