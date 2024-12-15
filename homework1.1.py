import datetime

def get_days_from_today(date):
    try:
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.datetime.today()
        days_difference = today_date.toordinal() - current_date.toordinal()
        return days_difference
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."
    except TypeError:
        return "Provided date is of an invalid type."


print (get_days_from_today("2021-10-09"))