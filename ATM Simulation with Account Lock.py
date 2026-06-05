#Question:
# ATM Simulation with Account Lock 
# Simulate a simple ATM system.
# 
# 
# User has 3 attempts to enter the correct PIN. done
# If PIN is correct, show menu (Withdraw, Deposit, Check Balance, Exit).
# If all attempts fail, block the account.
# while loop → PIN attempts
# if-elif-else → correct / incorrect / blocked
# Nested while → menu system
# Nested if → balance validation



print("*******ATM Simulation with Account Lock*********")

correct_pin="1234"
balance=10000
attempt=0
max_attempts=3

#PIN verification (while loop)
while attempt<max_attempts:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("\n PIN Verified Successfully!")
        
        #Nested while loop
        while True:
            print("\n------ ATM Menu ------ \n1. Withdraw \n2. Deposite \n3. Check Balance \n4. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                amount = float(input("Enter withdraw amount: "))
                
                # Nested if (balance validation)
                if amount <= balance:
                    balance -= amount
                    print(f"Withdrawal Successful! New Balance: {balance}")
                else:
                    print("Insufficient Balance!")
            
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                balance += amount
                print(f"Deposit Successful! New Balance: {balance}")
            
            elif choice == "3":
                print(f"Current Balance: {balance}")
            
            elif choice == "4": 
                print("Thank you for using ATM. Goodbye!")
                break
            
            else:
                print("Invalid Option! Try Again.")
        
        break   
    
    else:
        attempt += 1
        remaining = max_attempts - attempt
        print(f"Wrong PIN! Attempts left: {remaining}")

# Account Blocked
if attempt == max_attempts:
    print("\nAccount Blocked! Too many wrong attempts.")


