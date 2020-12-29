# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime

date_now = datetime.datetime.now()
print("It is currently {}.".format(str(date_now)))

new_date = date_now + datetime.timedelta(minutes=1000)
print("In 1000 minutes it will be {}.".format(str(new_date)))
