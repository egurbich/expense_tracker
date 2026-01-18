from utils import validate_date, validate_amount, validate_type

def add_transaction(ledger, transaction):
    if not validate_date(transaction["date"]):
      return False
    
    amount = validate_amount(transaction["amount"])
    if amount is None:
      return False
    
    transaction_type = validate_type(transaction["type"])
    if transaction_type is None:
      return False
    
    ledger.append(transaction)

    return True
    
def filter_by_type(ledger, transaction_type):
    result = [tx for tx in ledger if tx['type'] == transaction_type]
    return result

def filter_by_category(ledger, category):
    result = [tx for tx in ledger if tx['category'] == category]
    return result

def get_unique_categories(ledger):
    categories = set()
    for tx in ledger:
        categories.add(tx['category'])
    return list(categories)