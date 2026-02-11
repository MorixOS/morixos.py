import os
import platform
import time

filename = "os_data.txt"

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
username = None

print(rf"C:\Users\{username}>starting...")
time.sleep(1.5)
print(rf"C:\Users\{username}>loading bootloader...")
time.sleep(1.5)
print(rf"C:\Users\{username}>loading kernel...")
time.sleep(1.5)
clear_console()

login = True
current_user = None

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "os_data.txt")

username = None
password = None

try:
    with open(DATA_FILE, "r") as file:
        line = file.readline().strip()
        if line:
            parts = line.split(":")
            if len(parts) == 2:
                username, password = parts
except FileNotFoundError:
    pass

while login:
    if username:
        print(rf"C:\Users\{username}>Welcome back {username}!")
        pw_input = input(rf"C:\Users\{username}>Please enter your password: ")
        if pw_input == password:
            print(rf"C:\Users\{username}>Login successful!")
            current_user = username
            login = False
            time.sleep(1)
        else:
            print(rf"C:\Users\{username}>Incorrect password. Try again!")
            time.sleep(1)
    else:
        username = input(r"C:\Users\?>Please enter your name: ")
        password = input(rf"C:\Users\{username}>Please set your password: ")
        with open(DATA_FILE, "w") as file:
            file.write(f"{username}:{password}\n")
        clear_console()
        print(rf"C:\Users\{username}>Account created successfully. Welcome to MorixOS, {username}!")
        current_user = username
        login = False
        time.sleep(1)


os_on = True
while os_on == True:
    clear_console()
    print("MorixOS [Version 1.0]. For help type morix/help.")
    print("Wealthix Corporation. Alle Rechte vorbehalten.")
    print(rf"C:\Users\{username}> Welcome to MorixOS!")
    command = input(rf"C:\Users\{username}>")
    if command == "morix/help":
        print(rf"C:\Users\{username}>type morix/off to Shutdown.")
        print(rf"C:\Users\{username}>type morix/calculator for Calculator.")
        print(rf"C:\Users\{username}>type morix/games to see your Games.")
        print(rf"C:\Users\{username}>type morix/bank for the build in fake bank app.")
        print(rf"C:\Users\{username}>type morix/chrome for Browser.")
        input(rf"C:\Users\{username}>press enter to go back to home screen... ")
    if command == "morix/off":
        print(rf"C:\Users\{username}>shutting down...")
        time.sleep(1)
        os_on = False
    if command == "morix/calculator":
        print(rf"C:\Users\{username}>Welcome {username} to the MorixOS calculator!")
        print(rf"C:\Users\{username}>Available operations:")
        print(rf"C:\Users\{username}>1. Addition (+)")
        print(rf"C:\Users\{username}>2. Subtraction (-)")
        print(rf"C:\Users\{username}>3. Division (/)")
        print(rf"C:\Users\{username}>4. Multiplication (*)")

        choice = input(rf"C:\Users\{username}>Choose an operation (1-4): ").strip()

        num_count = int(
            input(rf"C:\Users\{username}>How many numbers do you want to use? (2-5): ")
        )

        if num_count < 2 or num_count > 5:
            print(rf"C:\Users\{username}>Invalid number of inputs. Exiting...")
            exit()

        numbers = []
        for i in range(1, num_count + 1):
            num = float(input(rf"C:\Users\{username}>Enter number {i}: "))
            numbers.append(num)

        result = numbers[0]

        if choice == "1":
            for n in numbers[1:]:
                result += n
            op_symbol = "+"
        elif choice == "2":
            for n in numbers[1:]:
                result -= n
            op_symbol = "-"
        elif choice == "3":
            for n in numbers[1:]:
                result /= n
            op_symbol = "/"
        elif choice == "4":
            for n in numbers[1:]:
                result *= n
            op_symbol = "*"
    elif command == "morix/games":
        clear_console()
        print(rf"C:\Users\{username}>These are your games!")
        print(
            f"list\nof\ngames"
        )
        game = input(fr"C:\Users\{username}>Which game do you want to play?: ")
        if game == "Game Name":
            os.startfile(r"C:\Path\to\Game.exe")
    
    elif command == "morix/bank":
        filename = "bank_data.txt"
        balance = 0

        users = {}
        account_numbers = set()

        try:
            with open("filename", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # leere Zeilen überspringen

                    parts = line.split(":")
                    if len(parts) != 4:
                        print("Überspringe kaputte Zeile:", line)
                        continue

                    name, password, acc_number, balance = parts
                    users[name] = {
                        "password": password,
                        "account_number": acc_number,
                        "balance": int(balance)
                    }
                    account_numbers.add(acc_number)
        except FileNotFoundError:
            pass

        print("Welcome to MorixOS Bank!")
        login_signup = input("Do you want to log in or sign up?: ")
        bank_on = True

        while bank_on:
            if login_signup == "sign up":
                name = input("What is your name?: ")
                password = input("Please enter a password: ")
                acc_number = input("Enter an account number: ")

                if acc_number in account_numbers:
                    print("Account number already exists!")
                else:
                    users[name] = {
                        "password": password,
                        "account_number": acc_number,
                        "balance": balance,
                    }

                    with open("filename", "a") as file:
                        file.write(f"{name}:{password}:{acc_number}:{balance}\n")

                    print(f"Welcome {name}!")
                    print("How can I help you?")
                    print("Deposit")
                    print("Withdraw")
                    print("Balance")
                    print("Transfer")
                    print("End Program")

                    chose = input("What do you want to do?: ")

                    if chose == "balance" or chose == "Balance":
                        print(f"Your balance is {balance}$!")
                        on_off = input("Do you want to end the program?: ")

                        if on_off == "yes" or on_off == "Yes":
                            print("Ending...")
                            time.sleep(1)
                            bank_on = False
                        else:
                            print("Going back to the home menu...")
                            time.sleep(1)

                    elif chose == "deposit" or chose == "Deposit":
                        amount = int(input("How much do you want to deposit?: "))
                        users[name]["balance"] += amount
                        print(
                            f"You deposited {amount}$. You now have {users[name]['balance']}$."
                        )
                        on_off = input("Do you want to end the program?: ")

                        if on_off == "yes" or on_off == "Yes":
                            print("Ending...")
                            time.sleep(1)
                            bank_on = False
                        else:
                            print("Going back to the home menu...")
                            time.sleep(1)
                    
                    elif chose == "withdraw" or chose == "Withdraw":
                        amount = int(input("How much do you want to withdraw?: "))
                        if amount <= users[name]["balance"]:
                            users[name]["balance"] -= amount
                            print(f"You withdrew {amount}$. You now have {users[name]['balance']}.")
                        else:
                            print("You don't have enough money!")
                            time.sleep(1)

                    elif chose == "transfer" or chose == "Transfer":
                        print("This function isn't available...")
                        time.sleep(1)

                    elif chose in ["end", "End", "End Program", "end program"]:
                        end = input("Do you really want to end the program?: ")
                        if end == "yes" or end == "Yes":
                            print("Ending...")
                            time.sleep(1)
                            bank_on = False
                        else:
                            print("Program will not end.")
                            time.sleep(1)

            elif login_signup == "login":
                print("Welcome to the login page!")
                print(f"Welcome {name}!")
                print("How can I help you?")
                print("Deposit")
                print("Withdraw")
                print("Balance")
                print("Transfer")
                print("End Program")

                chose = input("What do you want to do?: ")

                if chose == "balance" or chose == "Balance":
                    print(f"Your balance is {balance}$!")
                    on_off = input("Do you want to end the program?: ")

                    if on_off == "yes" or on_off == "Yes":
                        print("Ending...")
                        time.sleep(1)
                        bank_on = False
                    else:
                        print("Going back to the home menu...")
                        time.sleep(1)

                elif chose == "deposit" or chose == "Deposit":
                    amount = int(input("How much do you want to deposit?: "))
                    users[name]["balance"] += amount
                    print(
                        f"You deposited {amount}$. You now have {users[name]['balance']}$."
                    )
                    time.sleep(1)

                elif chose == "withdraw" or chose == "Withdraw":
                    amount = int(input("How much do you want to withdraw?: "))
                    if amount <= users[name]["balance"]:
                        users[name]["balance"] -= amount
                        print(
                            f"You withdrew {amount}$. You now have {users[name]['balance']}."
                        )
                    else:
                        print("You don't have enough money!")
                        time.sleep(1)
                elif chose == "transfer" or chose == "Transfer":
                    print("This function isn't available...")
                    time.sleep(1)

                elif chose in ["end", "End", "End Program", "end program"]:
                    end = input("Do you really want to end the program?: ")
                    if end == "yes" or end == "Yes":
                        print("Ending...")
                        time.sleep(1)
                        bank_on = False
                    else:
                        print("Program will not end.")
                        time.sleep(1)
                else:
                    print("Login failed.")
        
    elif command == "morix/browser":
        os.startfile(r"C:\path\to\browser.exe")
