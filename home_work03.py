# Task 1: Function to calculate days to the date from today

from datetime import datetime
def get_days_from_today(date_str):
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return ("Invalid date format. Use YYYY-MM-DD")
    today = datetime.today()
    diff = (parsed_date.date() - today.date()).days
    return int(diff)

print(get_days_from_today("2025-07-06") ) # Example usage

# Task 2: Function to generate a set of unique random numbers

import random

def get_numbers_ticket(min, max, quantity):
    number_set = set()

    if min >= 1 and max <= 1000 and (max - min) >= quantity:
        while len(number_set) < quantity:
            number_set.add(random.randint(min, max))
        return sorted(number_set)
    else:
        return number_set
    
get_numbers_ticket(1, 1000, 5)  # Example usage


# Task 3: Function to normalize phone numbers

import re
def normalize_phone(phone_number):
    phone_number = re.sub(r'\D+', '', phone_number)
        
    if len(phone_number) == 10:
        return '+38' + phone_number
    elif len(phone_number) == 12 and phone_number.startswith('380'):
        return '+' + phone_number
    else:
        return "Invalid phone number format"
    
    
