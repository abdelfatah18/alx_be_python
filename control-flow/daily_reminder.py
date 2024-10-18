# daily_reminder.py

def get_task_details():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    # Create a base reminder message based on priority using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = "Invalid priority entered."
            return reminder  # Return early if priority is invalid

    # Use if statements to modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    return reminder

def main():
    # Get task details from the user
    task, priority, time_bound = get_task_details()
    
    # Create and print the customized reminder
    reminder = create_reminder(task, priority, time_bound)
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
