#Program to print calendar
import calendar


year = int(input("Year: "))
month = int(input("Month: "))
print(" ")
print(calendar.month(year, month))
print("Have a nice month!")