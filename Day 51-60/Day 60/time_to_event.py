import datetime


today = datetime.date.today()


print("Event Countdown Timer\n")
event_name= input("Please enter the name of the event\n> ")
print("Please enter the date of the event DD.MM.YYYY")
day,month,year = map(int,input("> ").split('.'))
event = datetime.date(year=year,month=month,day=day)

difference= event -today

if event > today:
    print(f"{event_name} is in {difference.days} day(s) :)")
elif event < today:
    print(f"{event_name} was {abs(difference.days)} Day(s) ago")
elif event == today:
    print(f"{event_name} is Today 🎉🎉")
