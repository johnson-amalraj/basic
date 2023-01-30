import datetime # date time module
import pytz # timezone

# refer GitHub for 'Maya' time module
today = datetime.date.today()
print(today)

birthday = datetime.date(1996, 1, 18)
cal = (today - birthday).days
print(cal)

date_delta = datetime.timedelta(days=20)
print(today + date_delta)
# Monday - 0, Sunday - 6
print(today.month)
print(today.day)
print(today.year)
print(today.weekday())


time = datetime.time(8, 30, 7, 500)
# print(time)
# datetime.time (Y, M, D)
# datetime.time (H, M, S, MS)
# datetime.datetime (Y, M, D, H, M, S, MS)

hour_delta = datetime.timedelta(hours=5)
print(datetime.datetime.now())
print(datetime.datetime.now() + hour_delta)
# print(time + hour_delta)


zone = datetime.datetime.now(tz=pytz.UTC)
print(zone)
india = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
print(india)

# To print all timezone
# for zone in pytz.all_timezones:
#     print(zone)


# Formating
# %B -> Month, %d -> Date %Y -> Year
india = india.strftime('%B %d, %Y')
print(india)
# back to normal format like 2020-07-27 we can use strptime
# p -> parsing f-> formating
india = datetime.datetime.strptime('July, 27, 2020', '%B, %d, %Y')
print(india)
# repr() its print the object map