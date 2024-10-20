
from datetime import datetime ,timedelta
# Get current date and time
def display_current_datetime() :
  current_date= datetime.now()
  print("Current date and time:",current_date)
display_current_datetime()

def calculate_future_date():
  number_of_days=int(input("Enter the number of days to add to the current date:"))
  current_date=datetime.now()
  future_date=timedelta(number_of_days)+current_date
  print(future_date)
