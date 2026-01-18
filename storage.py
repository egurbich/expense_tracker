import csv

FILE = 'data/ledger.csv'
FIELDS = ["date", "type", "category", "amount", "note"]

def save_csv(path, ledger):
    try:
      with open(path, mode='w', newline='', encoding='utf-8') as file:
          writer = csv.DictWriter(file, fieldnames=FIELDS)
          writer.writeheader()

          for entry in ledger:
              writer.writerow(entry)

    except Exception:
        print("Error saving data")
    

def load_csv(path):
    ledger = []
    try:
      with open(path, mode='r', newline='', encoding='utf-8') as file:
          reader = csv.DictReader(file)
          for row in reader:
              row['amount'] = float(row['amount'])
              ledger.append(row)
    except FileNotFoundError:
        pass
    return ledger