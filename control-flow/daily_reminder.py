# daily_reminder.py
# Reminds user about a single task based on priority and time sensitivity

def main():
    # Step 1: Get user input
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Step 2: Match Case for priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered! Use high, medium, or low.")
            return  # Exit program if priority is invalid

    # Step 3: Modify message if task is time-bound
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message = "Note: " + message + ". Consider completing it when you have free time."
    else:
        print("Invalid time-bound input! Use yes or no.")
        return  # Exit if time-bound input is invalid

    # Step 4: Print the reminder
    print("\nReminder:", message)

if __name__ == "__main__":
    main()
