import os
from datetime import datetime

def ensure_dir(directory):
    """Create the directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def ordinal(n):
    """Return ordinal number string from integer, e.g. 1 -> '1st'."""
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def create_diary_entry():
    """Create a diary entry for today."""
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%B')  # Full month name
    day = int(today.strftime('%d'))  # Day as integer to generate ordinal
    time = today.strftime('%I:%M %p')  # Time in 12-hour clock

    day_with_suffix = ordinal(day)

    # Create filename in mm-dd-yyyy format
    file_date_format = today.strftime('%m-%d-%Y')
    file_name = f"{file_date_format}.txt"

    # Base diary directory
    base_dir = 'diary'

    # Create the directory structure
    year_dir = os.path.join(base_dir, year)
    month_dir = os.path.join(year_dir, month)
    day_file = os.path.join(month_dir, file_name)

    ensure_dir(year_dir)
    ensure_dir(month_dir)

    # Create and populate the day file if it doesn't exist
    if not os.path.exists(day_file):
        with open(day_file, 'w') as f:
            f.write(f'Today is {month} {day_with_suffix} {year} {time}')

    print(day_file)

if __name__ == '__main__':
    create_diary_entry()
