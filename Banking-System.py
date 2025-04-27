accounts = {
    "johndoe": {"password": "1234", "balance": 500.0},
    "janedoe": {"password": "abcd", "balance": 1000.0}
}

def create_account():
  while True:
    user_name = input("Enter your username: ")
    if user_name in accounts:
      print("\nUsername already exists. Try again.\n")
      continue
    password = input("Enter your password: ")
    balance = float(input("Enter initial deposit: "))  
    accounts[user_name] = {"password": password, "balance": balance}
    print("Account created successfully!")
    break  # Exit the loop after successful creation

def log_in():
  while True:
    user_name = input("Enter your username: ")
    if user_name in accounts:
      # Give the user 3 tries to enter the correct password
      for i in range(3):
       password = input("Enter your password: ")
       if password == accounts[user_name]["password"]:
        print("Login successful!")
        return user_name
       else:
        print("Incorrect password.")
        print("Too many failed attempts. Exiting login.")
        return None
    else:
      print("Username not found.")

def check_balance(user_name):
    print("Your balance is: $" + str(accounts[user_name]['balance']))

def withdraw(user_name):
    amount = float(input("How much do you want to withdraw?: "))
    if accounts[user_name]['balance'] < amount:
        print("Insufficient funds!")
    else:
        accounts[user_name]['balance'] -= amount
        print("Withdrawal successful.")
        print("Your new balance is: $" + str(accounts[user_name]['balance']))

def deposit(user_name):
    amount = float(input("How much do you want to deposit?: ")) 
    accounts[user_name]['balance'] += amount
    print("Deposit successful.")
    print("Your new balance is: $" + str(accounts[user_name]['balance']))

def main():
  while True:

    new = input("Do you want to create a new account? (Y/N): ").upper()
        
    if new == "Y":
      create_account()
        
    elif new == "N":
      user = log_in()
      if user:
      # Put the menu inside a loop so user can perform multiple actions
        while True:
          print("\nMenu:")
          print("1) Check Balance")
          print("2) Withdraw")
          print("3) Deposit")
          print("4) Log Out")          

          choice = input("Enter your choice: ")
          if choice == "1":
            check_balance(user)
          elif choice == "2":
            withdraw(user)
          elif choice == "3":
            deposit(user)
          elif choice == "4":
            print("Logging out...")
            break  # Exit to main loop after logout
          else:
            print("Invalid input!")
      else:
        print("Login failed.")
    else:
      print("Invalid input. Please enter Y or N.")

main()
