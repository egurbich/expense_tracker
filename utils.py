import datetime

DATE_FORMAT = "%Y-%m-%d"

def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False
    
def validate_amount(amount_string):
    
    try: 
      amount = float(amount_string)
      if amount > 0:
          return amount
      else:
          return None
    except ValueError:
      return None

def validate_type(type_string):
    type_lower = type_string.lower()
    if type_lower == "income" or type_lower == "expense":
        return type_lower
    else:
        return None
