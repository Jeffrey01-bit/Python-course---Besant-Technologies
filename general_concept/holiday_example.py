import holidays
from holidays.countries import India

indian_holidays= holidays.country_holidays(country='India',years=2026)
print(indian_holidays)
for date, name in indian_holidays.items():
    print(date, name)

USA_holidays= holidays.country_holidays(country='USA',years=2026)
print("USA_holidays: ",USA_holidays)
for date, name in USA_holidays.items():
    print(date, name)