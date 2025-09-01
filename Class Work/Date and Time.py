from datetime import date,datetime,timedelta

today=date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())


now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


print(now.strftime("%y-%m-%d"))
print(now.strftime("%y/%m/%d"))
print(now.strftime("%y %b %d"))
print(now.strftime("%B %d,%Y"))
print(now.strftime("%H:%M:%S %a"))
print(now.strftime("%H:%M:%S %A"))
print(now.strftime("%H:%M:%S %A %p"))

print(now.strftime("%A,%B %d,%Y|%H:%M:%S %p"))

nextweek=today + timedelta(days=7)
after30min=now + timedelta(minutes=30)
print(after30min)
print(nextweek)
