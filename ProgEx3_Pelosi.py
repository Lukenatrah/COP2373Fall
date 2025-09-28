from functools import reduce

def main():
    expenses = []
    
    # Collect expenses from the user
    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ")
        if expense_type.lower() == "done":
            break
        try:
            amount = float(input(f"Enter amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    if not expenses:
        print("No expenses entered.")
        return

    # Total expense using reduce
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Highest expense using reduce
    highest = reduce(lambda acc, item: acc if acc[1] >= item[1] else item, expenses)

    # Lowest expense using reduce
    lowest = reduce(lambda acc, item: acc if acc[1] <= item[1] else item, expenses)

    # Display results
    print("\nExpense Report")
    print("--------------------")
    print(f"Total expenses: ${total:.2f}")
    print(f"Highest expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()
