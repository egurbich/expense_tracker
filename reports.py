def get_total_income(ledger):
  total = 0
  for tx in ledger:
      if tx['type'] == 'income':
          total += tx['amount']
  return total

def get_total_expenses(ledger):
  total = 0
  for tx in ledger:
      if tx['type'] == 'expense':
          total += tx['amount']
  return total

def get_balance(ledger):
   return get_total_income(ledger) - get_total_expenses(ledger)

def get_expenses_by_category(ledger):
  result = {}
  for tx in ledger:
      if tx['type'] == 'expense':
          category = tx['category']
          if category in result:
              result[category] += tx['amount']
          else:
              result[category] = tx['amount']
  return result