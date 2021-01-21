import datetime
import pytz
from pytz import timezone

# current date
date_now = datetime.datetime.now().date
# current time
time_now = datetime.datetime.now().time
# current date time
datetime_now = datetime.datetime.now()
# current day
day_now = date_now.day
# current month
month_now = date_now.month
# current day
year_now = date_now.year

# new date
date_new = datetime.date(1990, 1, 31)
# new time
time_new = datetime.time(9, 30, 00)
# new date time
date_new = datetime.datetime(1990, 1, 31, 9, 59, 00)

# today
today = datetime.datetime.now().date()
today = datetime.date.today()

# yesterday
yesterday = datetime.date(today.year, today.month, today.day-1)
yesterday = datetime.datetime.now().date().replace(day=datetime.datetime.now().day-1)

# tomorrow
tomorrow = datetime.date(today.year, today.month, today.day+1)
tomorrow = datetime.datetime.now().date().replace(day=datetime.datetime.now().day+1)

# formt date in string.
date_formatted = date_now.strftime('%d/%m/%Y')
time_formatted = date_now.strftime('%H:%M:%S')
datetime_formatted = date_now.strftime('%d/%m/%Y %H:%M:%S')

# string to datetime
datetime_str = "01/12/2008 09:40"
datetime_str_to_date = datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

# list all timezone
for zone in pytz.all_timezones:
    print(zone)

# define timezone
timezone_here = timezone("America/Sao_Paulo")
timezone_buenos = timezone("America/Argentina/Buenos_Aires")
timezone_pacific = timezone("US/Pacific")

time_tz_here = datetime.datetime.now().astimezone(timezone_here)
time_tz_buenos = datetime.datetime.now().astimezone(timezone_buenos)
time_tz_pacific = datetime.datetime.now(tz=timezone_pacific)

print("Time Here with TZ")
print(time_tz_here)
print("Time Buenos Aires with TZ")
print(time_tz_buenos)
print("Time Pacific with TZ")
print(time_tz_pacific)
