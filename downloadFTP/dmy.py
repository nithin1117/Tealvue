import argparse
import datetime
import sys
import calendar


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date", help="name of the user")
args = vars(ap.parse_args())
dmy = args["date"]

def AutoDate():
    from datetime import date
    today = date.today()
    mon = today.strftime("%b")
    dmy = today.strftime("%d" + mon + "%Y")
    return dmy


if dmy == None:
    dmy= AutoDate()
    
else:
    while True:
        day = dmy
        try :
            day = datetime.datetime.strptime(day, "%d/%m/%Y")
            break
        except ValueError:
            print('Error: Invalid Date Format, Try DD/MM/YYY')
            sys.exit()

    mon = calendar.month_abbr[int(day.month)]
    DMY = (f"{day.day}" + mon + f"{day.year}")




val = "val" + dmy
print(val)
