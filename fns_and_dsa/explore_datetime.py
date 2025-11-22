# explore_datetime.py
"""
Explore Python's datetime module.
- display_current_datetime() -> prints current date/time and stores it in `current_date`
- calculate_future_date(days) -> computes future date, stores in `future_date`, and returns it
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtain the current date and time, save it to `current_date`,
    and return it formatted as "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted

def calculate_future_date(days):
    """
    Add `days` (int) to the current date and return the future date.
    Saves result in `future_date` variable and prints it as "YYYY-MM-DD".
    """
    # ensure we work with the current date/time (consistent with part 1)
    today = datetime.now()
    # create the timedelta from the passed days
    delta = timedelta(days=days)
    # compute future date/time
    future_date = today + delta
    # We usually only need the date portion here
    future_date_only = future_date.date()
    print(f"Future date: {future_date_only.isoformat()}")
    # return the future_date (datetime) and the date-only for flexibility
    return future_date, future_date_only

def prompt_for_days():
    """
    Prompt the user for an integer number of days.
    Keep asking until a valid integer is entered.
    Returns the integer.
    """
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(user_input)
            return days
        except ValueError:
            print("Please enter a valid integer (e.g., 10 or -5). Try again.")

if __name__ == "__main__":
    # Part 1: show current date/time
    display_current_datetime()

    # Part 2: ask user for days, calculate and show future date
    days_to_add = prompt_for_days()
    calculate_future_date(days_to_add)