# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder variable
reminder = ""

# Generate the reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' priority level not recognized. Please use high, medium, or low."

# Adjust the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Finalize the output
final_reminder = f"Customized Reminder:\nTask: {task}\nPriority Level: {priority.capitalize()}\n{reminder}"

# Print the customized reminder with clear instructions
print(final_reminder)
