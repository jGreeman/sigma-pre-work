import datetime

print(datetime.date.today())

def input_date():
    date = input('Please enter a date in the format: YYYY-MM-DD')
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def date_diff(date):
    first_date = datetime.datetime.today()
    second_date = date
    difference = first_date - second_date
    difference_days = difference.days
    return round(difference_days/365.25)

# print("The difference in years to the nearest whole number is:", date_diff(datetime.date(2015, 3, 3)))
print('The difference in dates in years is:', date_diff(input_date()))
