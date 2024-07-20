# program to add, subtract 2 years | 5 months | 7 days to a date

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
print(today)

# new_date = today + 7  ERROR

new_date = today + relativedelta(years=2, months=5, days=7)
print(new_date.date())
print(new_date.strftime('%d-%m-%Y'))