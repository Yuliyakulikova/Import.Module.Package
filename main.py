import application.db.people
from application.salary import calculate_salary
import pytz
import datetime

tz_berlin = pytz.timezone("Europe/Berlin")
dt_berlin =datetime.datetime.now(tz_berlin)

if __name__ == '__main__':
    print(dt_berlin)
    application.db.people.get_employees()
    calculate_salary()