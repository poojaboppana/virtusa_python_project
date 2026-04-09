import csv
import os
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FILE = "expenses.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount", "description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Bills/Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")

def view_expenses():
    print("\nAll Expenses:")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])

    print(f"\nTotal Expense for {month}: {total}")

def category_analysis():
    categories = {}

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            categories[category] = categories.get(category, 0) + amount

    if not categories:
        print("No data available.")
        return

    highest = max(categories, key=categories.get)
    print(f"\nHighest Spending Category: {highest}")

    plt.figure()
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Category-wise Expense Distribution")
    plt.savefig("expense_chart.png")
    print("Chart saved as expense_chart.png")

def generate_insights():
    categories = {}
    total = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            total += amount
            categories[category] = categories.get(category, 0) + amount

    if total == 0:
        print("No data to analyze.")
        return

    highest = max(categories, key=categories.get)
    highest_value = categories[highest]

    print("\nInsights:")
    print(f"Total Spending: {total}")
    print(f"Highest Category: {highest} ({highest_value})")

    if highest_value > 0.4 * total:
        print(f"You are spending too much on {highest}. Try to reduce it.")
    else:
        print("Your spending is balanced.")

    if "Food" in categories and categories["Food"] > 0.3 * total:
        print("Consider reducing outside food expenses.")

    if "Travel" in categories and categories["Travel"] > 0.3 * total:
        print("Try optimizing travel costs.")

def main():
    while True:
        print("\nSmart Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis (Chart)")
        print("5. Generate Insights")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            generate_insights()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

main()