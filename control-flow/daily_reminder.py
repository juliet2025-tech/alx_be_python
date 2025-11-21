# daily_reminder.py
# Reminds user about a single task based on priority and time sensitivity

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority entered! Use high, medium, or low.")
        return

    # Validate time-bound
    if time_bound not in ["yes", "no"]:
        print("Invalid time-bound input! Use yes or no.")
        return

    # Build the reminder exactly as ALX expects
    if time_bound == "yes":
        reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
    else:
        reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()

