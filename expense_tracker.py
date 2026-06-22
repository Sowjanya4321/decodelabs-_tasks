import datetime

print("=" * 40)
print("      EXPENSE TRACKER SYSTEM")
print("=" * 40)

expenses = []
total = 0

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        category = input("Enter Expense Category: ")

        try:
            amount = float(input("Enter Expense Amount: ₹"))

            expense = {
                "category": category,
                "amount": amount,
                "date": datetime.datetime.now().strftime("%d-%m-%Y")
            }

            expenses.append(expense)
            total += amount

            print("✅ Expense Added Successfully!")

        except ValueError:
            print("❌ Invalid Amount!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No Expenses Recorded Yet.")
        else:
            print("\n------ Expense History ------")

            for i, exp in enumerate(expenses, start=1):
                print(
                    f"{i}. {exp['category']} | ₹{exp['amount']} | {exp['date']}")

    elif choice == "3":
        print(f"\n💰 Total Expenses: ₹{total}")

    elif choice == "4":

        print("\n========== SUMMARY ==========")

        if len(expenses) == 0:
            print("No Expenses Recorded.")
        else:
            for exp in expenses:
                print(
                    f"{exp['category']} : ₹{exp['amount']} ({exp['date']})")

        print(f"\nTotal Spent: ₹{total}")
        print("Thank You For Using Expense Tracker!")
        break

    else:
        print("❌ Invalid Choice! Select 1-4")