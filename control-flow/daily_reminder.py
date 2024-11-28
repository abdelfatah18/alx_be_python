# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    valid_priorities = {"high", "medium", "low"}
    if priority not in valid_priorities:
        print("Invalid priority. Please enter high, medium, or low.")
        return

    # Generate the base reminder based on the priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."

    # Modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
        return

    # Display the reminder
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
