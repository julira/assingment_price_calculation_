import pandas as pd

with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/tickets_sold.csv','rb') as csvfile:
    f = pd.read_csv(csvfile)
with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/row_capacity.csv','rb') as csvfile:
    a = pd.read_csv(csvfile) 
    
##  Total_tickets_per_week_movie_row 
f['tickets']=1   
x=f.groupby(['movie','calendarweek','auditorium_row'])['tickets'].count()
print x

##Seat_load_factor_per_week_movie_row
x1 = x.to_frame().reset_index()
df=a.merge(x1)
df['load_factor']=df['tickets']/df['max_seats_per_row']
print df
#seat_load_factor_per_week_row

df.groupby(['calendarweek','auditorium_row'])['load_factor'].mean()