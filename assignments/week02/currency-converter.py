#Assignment : Currency-Converter

RATE = 35
print("Currency Converter")
print("1) THB to USD")
print("2) USD to THB")
choice = input("Chose conversion (1 or 2) : ")
amount = int(input("Enter amount : "))
if choice == "1":
    result = amount / RATE
    print(f"\nFomula: USD = THB / {RATE}")
    print(f"{amount:.2f} THB = {result:.2f} USD")

elif choice == "2":
    result = amount * RATE
    print(f"nFomula: THB = USD * {RATE}")
    print(f"{amount:.2f} USD = {result:.2f} THB")
else:
    print("Invaid choice")