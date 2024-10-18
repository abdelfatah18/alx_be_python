# daily_reminder.py

def get_task_details():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = "Invalid priority entered."

    if priority in ["high", "medium", "low"] and time_bound == "yes":
        message += " that requires immediate attention today!"
    elif priority in ["high", "medium", "low"] and time_bound == "no":
        message += ". Consider completing it when you have free time."

    return message

def main():
    while True:
        task, priority, time_bound = get_task_details()
        reminder = create_reminder(task, priority, time_bound)
        print("\nReminder:", reminder)

        # Ask if the user wants to add another task
        another = input("\nWould you like to enter another task? (yes/no): ").lower()
        if another != "yes":
            print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
            break

if __name__ == "__main__":
    main()

