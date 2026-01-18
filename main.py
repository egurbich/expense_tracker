from storage import FILE, save_csv, load_csv
from logic import add_transaction, filter_by_type, filter_by_category, get_unique_categories
from reports import get_total_income, get_total_expenses, get_balance, get_expenses_by_category


def display_menu():
    """Main menu"""
    print("\n" + "="*40)
    print("  EXPENSE TRACKER")
    print("="*40)
    print("1) Add transaction")
    print("2) List transactions")
    print("3) Summary report")
    print("4) Save and quit")
    print("="*40)


def add_transaction_menu(ledger):
    """Adds a transaction through the user interface"""
    print("\n--- Add Transaction ---")
    
    date = input("Enter date (YYYY-MM-DD): ").strip()
    trans_type = input("Enter type (income/expense): ").strip()
    category = input("Enter category: ").strip()
    amount_str = input("Enter amount: ").strip()
    note = input("Enter note (optional): ").strip()
    
    # Validate and convert amount
    from utils import validate_amount
    amount = validate_amount(amount_str)
    
    if amount is None:
        print("✗ Invalid amount!")
        return
    
    transaction = {
        "date": date,
        "type": trans_type,
        "category": category,
        "amount": amount,  # ← now this is a float!
        "note": note
    }
    
    if add_transaction(ledger, transaction):
        print("✓ Transaction added successfully!")
    else:
        print("✗ Failed to add transaction. Please check your input.")


def list_transactions_menu(ledger):
    """Shows all transactions with filtering options"""
    print("\n--- List Transactions ---")
    print("1) Show all")
    print("2) Filter by type")
    print("3) Filter by category")
    
    choice = input("Choose option: ").strip()
    
    transactions_to_show = ledger
    
    if choice == "2":
        trans_type = input("Enter type (income/expense): ").strip().lower()
        transactions_to_show = filter_by_type(ledger, trans_type)
    elif choice == "3":
        print("Available categories:", ", ".join(get_unique_categories(ledger)))
        category = input("Enter category: ").strip()
        transactions_to_show = filter_by_category(ledger, category)
    
    if not transactions_to_show:
        print("\nNo transactions found.")
        return
    
    print(f"\nFound {len(transactions_to_show)} transaction(s):")
    print("-" * 80)
    print(f"{'Date':<12} {'Type':<10} {'Category':<15} {'Amount':>10} {'Note'}")
    print("-" * 80)
    
    for tx in transactions_to_show:
        print(f"{tx['date']:<12} {tx['type']:<10} {tx['category']:<15} {tx['amount']:>10.2f} {tx.get('note', '')}")
    print("-" * 80)


def show_summary_menu(ledger):
    """Shows a summary report"""
    print("\n--- Summary Report ---")
    
    total_income = get_total_income(ledger)
    total_expenses = get_total_expenses(ledger)
    balance = get_balance(ledger)
    expenses_by_cat = get_expenses_by_category(ledger)
    
    print(f"\nTotal Income:    {total_income:>10.2f} UAH")
    print(f"Total Expenses:  {total_expenses:>10.2f} UAH")
    print(f"{'─' * 35}")
    print(f"Balance:         {balance:>10.2f} UAH")
    
    if expenses_by_cat:
        print("\n--- Expenses by Category ---")
        for category, amount in sorted(expenses_by_cat.items()):
            print(f"{category:<20} {amount:>10.2f} UAH")


def main():
    """Main function of the program"""
    print("Loading data...")
    ledger = load_csv(FILE)
    print(f"Loaded {len(ledger)} transaction(s).")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_transaction_menu(ledger)
        elif choice == "2":
            list_transactions_menu(ledger)
        elif choice == "3":
            show_summary_menu(ledger)
        elif choice == "4":
            print("\nSaving data...")
            save_csv(FILE, ledger)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()