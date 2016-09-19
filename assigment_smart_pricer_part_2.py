import pandas as pd

with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/tickets_sold.csv','rb') as csvfile:
    f = pd.read_csv(csvfile)
    print f
  with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/row_capacity.csv','rb') as csvfile:
    a = pd.read_csv(csvfile) 
    print a
##Seat_load_factor_per_week_movie_row
x1 = x.to_frame().reset_index()
print x1
df=a.merge(x1)

#seat_load_factor_per_week_row
df.groupby(['calendarweek','auditorium_row'])['load_factor'].mean()