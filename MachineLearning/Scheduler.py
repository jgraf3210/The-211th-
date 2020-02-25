import datetime
from datetime import date
import time
import calendar

# As of right now, this scheduler just runs until it's 4pm i.e 16:00
def schedule():
    while True:
        currentDate = datetime.datetime.now().date()
        currentDate = str(currentDate)
        currentDate.split(sep='-')
        year = (currentDate[0] + currentDate[1] + currentDate[2] + currentDate[3])
        month = currentDate[5] + currentDate[6]
        day = currentDate[8] + currentDate[9]
        if currentDate[5].startswith('0'):
            month = currentDate[6]
        if currentDate[6].startswith('0'):
            day = currentDate[9]
        currentHour = datetime.datetime.now().hour
        currentMinute = datetime.datetime.now().minute
        currentSecond = datetime.datetime.now().second
        datetime.datetime(int(year), int(month), int(day),
                          currentHour, currentMinute, currentSecond)
        currentDay = datetime.datetime.today().weekday()

        if currentDay == calendar.FRIDAY:
            print('STOCK MARKET CLOSED on [Friday]')
        if currentDay == calendar.SATURDAY:
            print('STOCK MARKET CLOSED on [Saturday]')
        if currentDay == calendar.SUNDAY:
            print('STOCK MARKET CLOSED on [Sunday]')
        if currentHour == 16 and currentMinute == 0:
           time.sleep(57600)
        print('Time is: ' + str(currentHour) + ':' + str(currentMinute))
        time.sleep(60)
schedule()