# daily_reminder.py
# Simplified daily reminder using Match Case, if statement, and loop

def main():
    while True:  # Loop to satisfy the "loops" requirement (even single iteration)
        # Step 1: Get user input
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        # Step 2: Use Match Case for priority
        match priority:
            case "high":
                reminder = f"'{task}' is a high priority task"
            case "medium":
                reminder = f"'{task}' is a medium priority task"
            case "low":
                reminder = f"'{task}' is a low priority task"
            case _:
                print("Invalid priority! Use high, medium, or low.")
                continue  # Ask again

        # Step 3: Use if statement to modify reminder if time-bound
        if time_bound == "yes":
            reminder = f"Reminder: {reminder} that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            print("Invalid input! Time-bound must be yes or no.")
            continue  # Ask again

        # Step 4: Print the reminder
        print("\n" + reminder)

        # Exit after one iteration since assignment asks for a single task
        break

if __name__ == "__main__":
    main()

