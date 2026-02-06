import random
import datetime
from datetime import date
def randomdate(start,end):
    random_sec = random.randint(0,int((end-start).total_seconds()))
    rdate=datetime.timedelta(seconds=random_sec)
    return start+rdate
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2021,1,1)
random_date= randomdate(start,end)
print("the random date between",start.date(),"and",end.date(),"is",random_date.date())