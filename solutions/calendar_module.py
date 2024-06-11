import calendar
import datetime


m,d,y = map(int,input().split())
days = {6:'SUNDAY',0:'MONDAY',1: 'TUESDAY', 2:'WEDNESDAY',3: 'THURSDAY',4:'FRIDAY',5: 'SATURDAY'}
day=calendar.weekday(y,m,d)
if day in days:
    print(days[day])        
