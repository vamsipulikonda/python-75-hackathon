import datetime 
a=datetime.datetime.now()

#to print time in seconds
print("the time is seconds now is: %s"%(a.strftime("%S")))

#print the current date
print("todays date is: %s"%(a.strftime("%x")))

#print the date in strftime
today = datetime.date.today()
print("the current date is: %s"%(today))

#print the current year
print("%s is the current year"%(a.strftime("%Y")))

#print the current month
print("%s is the current month"%(a.strftime("%B")))

#print the current number of week in the current year
b=datetime.date(2018, 12, 17).strftime("%V")
print("you are in %s week of the month"%(b))

#print the current number of the day 
print("you are in %s day of the year"%(a.strftime("%j")))

#print the current date of the month
print("the current date is: %s"%(a.strftime("%c")))


#print the current day of the month
print("todays is %s"%(a.strftime("%A")))

#print the prev year
print("your previosus year is -%d"%(a.today().year - 1))
