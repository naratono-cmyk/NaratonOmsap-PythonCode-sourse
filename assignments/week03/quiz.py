# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter your age: "))
if age >= 60:
    print("You are an Senior")
elif age >= 20:
    print("You are an Adult")
elif age >= 13:
    print("You are an Teenanger")
else:
    print("You are an Child")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            break
        elif choice == "1":
            print("Balance:", balance, "บาท")
        elif choice == "2":
            amout = float(input("ถอนเท่าไร?",))
            balance = balance - amout          
            print("")
        elif choice == "3":  
            amout = float(input("ฝากเท่าไร?",))
            balance = balance + amout       
else:
    print("Invalid PIN")

