def add_expense(category, amount, date):
    """Adds an expense to the expenses.txt file."""
    try:
        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount},{date}\n")
        print("Expense added successfully.")
    except IOError:
        print("Error: Could not write to expenses.txt.")

def view_expenses():
    """Displays all recorded expenses."""
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n--- All Expenses ---")
            for expense in expenses:
                category, amount, date = expense.strip().split(',')
                print(f"Category: {category}, Amount: {amount}, Date: {date}")
            print("--------------------")
    except FileNotFoundError:
        print("No expenses file found. Please add an expense first.")
    except IOError:
        print("Error: Could not read from expenses.txt.")

def get_total_expenditure():
    """Calculates and displays the total expenditure."""
    total_amount = 0.0
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                parts = expense.strip().split(',')
                if len(parts) == 3:  # Ensure correct format
                    try:
                        total_amount += float(parts[1])
                    except ValueError:
                        print(f"Warning: Invalid amount '{parts[1]}' found in an expense entry. Skipping.")
                else:
                    print(f"Warning: Malformed expense entry found: '{expense.strip()}'. Skipping.")
        print(f"\nTotal Expenditure: {total_amount:.2f}")
    except FileNotFoundError:
        print("No expenses file found. Total expenditure is 0.")
    except IOError:
        print("Error: Could not read from expenses.txt to calculate total.")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Get Total Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            get_total_expenditure()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()