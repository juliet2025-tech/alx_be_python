#!/usr/bin/env python3

import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted

def calculate_future_date(days):
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    print(display_current_datetime())
    print(calculate_future_date(7))

