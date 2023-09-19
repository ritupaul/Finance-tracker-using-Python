import argparse
import datetime

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Record item information and add it to a ledger file")

    # Define command-line arguments
    parser.add_argument("item_name", type=str, help="Name of the item")
    parser.add_argument("category", type=str, help="Category of the item")
    parser.add_argument("amount", type=float, help="Amount of the item")
    parser.add_argument("--ledger", "-l", type=str, default="ledger.txt", help="Ledger file name (default: ledger.txt)")

    # Parse the arguments
    args = parser.parse_args()

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Format the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Create or open the ledger file in append mode
    with open(args.ledger, "a") as ledger_file:
        # Write the item information to the ledger
        ledger_file.write(f"Date/Time: {formatted_datetime}\n")
        ledger_file.write(f"Item Name: {args.item_name}\n")
        ledger_file.write(f"Category: {args.category}\n")
        ledger_file.write(f"Amount: {args.amount:.2f}\n")
        ledger_file.write("-" * 20 + "\n")  # Separator

    print(f"Item information added to {args.ledger}")

if __name__ == "__main__":
    main()
