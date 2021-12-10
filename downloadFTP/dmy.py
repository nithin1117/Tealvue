import datetime
import sys
import calendar

while True:
    day = input('Enter date(dd/mm/yy):')
    try :
        day = datetime.datetime.strptime(day, "%d/%m/%Y")
        break
    except ValueError:

        day = input('Error: Try in the format dd/mm/yyyy:')
        try:
            day = datetime.datetime.strptime(day, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid Input, Exited")
            sys.exit()

mon = calendar.month_abbr[int(day.month)]
DMY = (f"{day.day}" + mon + f"{day.year}")
print(DMY)




# #today's date
# from datetime import date

# today = date.today()
# mon = today.strftime("%b")

# DMY = today.strftime("%d" + mon + "%Y")

# print(DMY)

