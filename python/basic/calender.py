import calendar
# TODO date and time pkg 

# Print calendar for specified year 
# calendar(year,width,length,spacing,column)
print(calendar.calendar(2020,3,1,4,3))


# Print calendar for specified month 
# month(year,month)
print(calendar.month(2020,4))

# Print calendar in array format 
# monthcalendar(year,month)
print(calendar.monthcalendar(2020,4))

# Print week days in string 
# weekheader(string length)
print(calendar.weekheader(3))

# Print a day for specified date 
# weekday(year,month,date)
print(calendar.weekday(2020,4,4))

# Print specified year is leap or not 
print(calendar.isleap(2020))

# Print leap days between specified years
# It take 2020 to 2029
# leapdays(from,to)
print(calendar.leapdays(2020,2030))