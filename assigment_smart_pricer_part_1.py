import pandas as pd

with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/tickets_sold.csv','rb') as csvfile:
    f = pd.read_csv(csvfile)
for row in f: print row
    print f
   with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/row_capacity.csv','rb') as csvfile:
    a = pd.read_csv(csvfile) 
    print a
 ##  Total_tickets_per_week_movie_row 
 f['tickets']=1   
x=f.groupby(['movie','calendarweek','auditorium_row'])['tickets'].count()
print x

  