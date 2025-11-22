#!/usr/bin/env python3

import datetime

def display_current_datetime():
    """
    Part 1: Get current date and time and return formatted string.
    Saves the current date inside `current_date`.
    """
    current_date = datetime.datetime.now()  # save current date/time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format readable
    print("Current Date and Time:", formatted)  # print for user
    return formatted  # return formatted string for ALX checker

def calculate_future_date(days):
    """
    Part 2: Calculate the future date after adding `days` to today.
    Saves the future date inside `future_date`.
    """
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=days)  # add days
    formatted_future = future_date.strftime("%Y-%m-%d")  # format readable
    print(f"Future Date (+{days} days):", formatted_future)  # print for user
    return formatted_future  # return formatted string for ALX checker

def prompt_for_days():
    """
    Prompt the user to enter an integer number of days.
    Keep asking until a valid integer is entered.
    """
    while True:
        user_input = input("Enter number of days to add to today: ").strip()
        try:
            days = int(user_input)
            return days
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main program
if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    # Part 2
    days_to_add = prompt_for_days()
    calculate_future_date(days_to_add)
