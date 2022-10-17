from datetime import date
import datetime
import calendar


today = date.today()

#1
print(today.strftime("%a %d %b %y"))

#2
xmas = date(2022, 12, 25)
days_left = xmas - today
print(f"Det är {days_left.days} dagar till julafton")


#3
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#4
days_in_month= calendar.monthrange(today.year, today.month)[1]
print(days_in_month)
