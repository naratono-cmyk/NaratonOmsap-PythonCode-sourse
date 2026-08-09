prices = []
bought_items = []
total_spent = 0

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))
print()

for i in range(6):
    if total_spent + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} -> buy")
        total_spent += prices[i]
        bought_items.append(prices[i])
    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")

    print(f"Current total = {total_spent}\n")

remaining_budget = budget - total_spent
print("Bought items:", bought_items)
print("Total spent:", total_spent)
print("Remaining budget:", remaining_budget)