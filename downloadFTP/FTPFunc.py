from ftplib import FTP
import gzip
import shutil
import argparse
import os

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
    dmy = AutoDate()
else:
    import datetime
    import calendar
    import sys

    while True:
        day = dmy
        try:
            day = datetime.datetime.strptime(day, "%d/%m/%Y")
            break
        except ValueError:
            print('Error: Invalid Date Format, Try DD/MM/YYYY')
            sys.exit()

    mon = calendar.month_abbr[int(day.month)]
    dmy = (f"{day.day}" + mon + f"{day.year}")


if dmy[1].isalpha():
    dmy = dmy.zfill(9)
else:
    pass


def ftpfile(dmy, num):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')
    path = '/Common/NTNEAT'
    ftp.cwd(path)
    try:
        key = 'FTPFILES'
        dir = os.getenv(key) + "/"
        # dir = "/home/nithin/Documents/sample/new/check/"
        try:
            if num == 1: fName = "contract.gz_" + dmy
            if num == 2: fName = "nnf_participant.gz_" + dmy
            if num == 3: fName = "nnf_security.gz_" + dmy
            if num == 4: fName = "participant.gz_" + dmy
            if num == 5: fName = "security.gz"
            if num == 6: fName = "spd_contract.gz"

            pathDir = dir + fName
            ftp.retrbinary("RETR " + fName, open(pathDir, 'wb').write)
            ftp.close()

            with open(pathDir, 'rb') as f_in:
                with gzip.open(pathDir + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

        except:
            print("Error: File not found for particular date in FTP")
            return "error"
    except:
        print("Error: path location had not prefered")
        print("run 'sudo gedit /etc/environment' and set 'FTPFILES = *desired directory*'")
        sys.exit() 


check = ftpfile(dmy, 1)

if check != "error":
    for i in range(2, 7):
        ftpfile(dmy, i)
    print("Downloaded and extracted!")
else:
    key = 'FTPFILES'
    dir = os.getenv(key) + "/"
    if os.path.exists(dir):
        os.remove("demofile.txt")
