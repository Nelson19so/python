import time

def account_balance_and_deposit_only():
    while True:
        try:
            balance = 700000000.00
            banks = ['fidelity bank', 'first bank', 'diamond bank', 'access bank']
            print("your balance is ${:,}".format(balance))

            # for user input method
            deposit = int(input("How much are you transferring: "))
            deposit_name = input("Transfer to: ")
            bank = input("Bank: ")
            if bank not in banks:
                print("Please enter a valid bank name and try again.")
                break

            # BALANCE
            balance = balance - deposit

            #rest
            print("transfer successful")
            print("you have transferred ${:,}".format(deposit), "to", deposit_name.upper())
            print("you have made a deposit of {:,}".format(deposit))
            print("your balance is: ${:,} ".format(balance))
            break
        except ValueError:
            print("ERROR trying to pass information")
            print("Try again, Something went wrong")

account_balance_and_deposit_only()


