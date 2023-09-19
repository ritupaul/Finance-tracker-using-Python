def read_ledger(ledger_file):
    ledger_data = {}

    try:
        with open(ledger_file, "r+") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    date, item_name, category, amount_str = parts
                    amount = float(amount_str)
                    
                    if category not in ledger_data:
                        ledger_data[category] = 0.0

                    ledger_data[category] += amount

    except FileNotFoundError:
        print(f"Ledger file '{ledger_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return ledger_data

def print_summary(ledger_data):
    print("Summary of Expenses:")
    for category, total_amount in ledger_data.items():
        print(f"{category}: ${total_amount:.2f}")

def main():
    ledger_file = "./my_ledger.txt"  # Replace with the path to your ledger file

    ledger_data = read_ledger(ledger_file)
    print_summary(ledger_data)

if __name__ == "__main__":
    main()
