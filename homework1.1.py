import datetime

def get_days_from_today(date):
    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    today_date = datetime.datetime.today()
    days_difference = today_date.toordinal() - current_date.toordinal()
    return days_difference

print (get_days_from_today("2021-10-09"))