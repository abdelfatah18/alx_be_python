# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate reminder based on priority using if statements
if priority == "high":
    reminder = f"'{task}' is a high priority task."
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task."
elif priority == "low":
    reminder = f"'{task}' is a low priority task."
else:
    reminder = "Invalid priority level. Please enter high, medium, or low."
    print(reminder)
    exit()

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()

# Display the customized reminder
print(reminder)

