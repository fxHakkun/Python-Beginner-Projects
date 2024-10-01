#Display holidays of your country

import holidays
import datetime

def main():
    isholidays = holidays.MY(years=2024, language = "ms_MY").items()
    istoday = datetime.datetime.now()

    print("List of holidays in Malaysia:")
    for date,day in sorted(isholidays): #to get to next holidays in line
        print(date,day)

    print("Today is", istoday.strftime("%A"), "and the date is", istoday.date())
    print("Next holiday will be on",date, "which is", day)
    holidaysnumber = date - istoday.date() #get the days from holidays
    hoursremain = 0 if (24 - int(istoday.strftime("%H"))) == 24 else (24 - int(istoday.strftime("%H"))) # to avoid time conversion turn 24-00 = 24(which is 24hr format) where it should be 0
    holidayshours = 0 if ((holidaysnumber.days * 24) + hoursremain) == 24 else ((holidaysnumber.days * 24) + hoursremain) #get the total hours from holidays and same process as above(paranoid lol)
    print("Holiday is in", holidaysnumber.days, "days and about", holidayshours, "hours")

if __name__ == "__main__":
    main()




