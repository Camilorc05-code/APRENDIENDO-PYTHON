### DATES ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

timestamp = now.timestamp()

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

from datetime import time

currente_time = time(21, 4, 0)

print(currente_time.hour)
print(currente_time.minute)
print(currente_time.second)

from datetime import date

currente_date = date.today()

print(currente_date.year)
print(currente_date.month)
print(currente_date.day)

currente_date = date(2028, 7, 3)

print(currente_date.year)
print(currente_date.month)
print(currente_date.day)

currente_date = date(currente_date.year, currente_date.month + 1, currente_date.day)

print(currente_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - currente_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(431, 123, 100, weeks = 15)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta % start_timedelta)