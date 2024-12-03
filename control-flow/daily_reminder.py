# daily_reminder.py

def get_task_info():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    # Match case to determine the priority level
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level entered."
    
    # Modify reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += " (Invalid input for time-bound task.)"
    
    return reminder

def main():
    task, priority, time_bound = get_task_info()
    reminder = generate_reminder(task, priority, time_bound)
    # Ensure the reminder is printed with the exact message required
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()
