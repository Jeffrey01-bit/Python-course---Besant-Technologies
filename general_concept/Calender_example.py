import calendar
import datetime as dt
print(calendar.calendar(2026))
print(calendar.month(2026,1))

current_date= dt.date.today()
print(current_date)
current_year= current_date.year
current_month= current_date.month
print(calendar.calendar(current_year))
print(calendar.month(current_year,current_month))
future_date= current_date + dt.timedelta(days=200)
print(future_date)

pre_month= current_date - dt.timedelta(days=30)
future_month= future_date + dt.timedelta(days=30)
print(calendar.month(pre_month.year,pre_month.month))
print(calendar.month(pre_month.year,future_month.month))

