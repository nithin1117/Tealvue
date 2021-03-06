from ftplib import FTP
import gzip
import shutil
import argparse
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date")
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
    
    
    day = dmy
    try:
        day = datetime.datetime.strptime(day, "%d/%m/%Y")
        
    except ValueError:
        print('Error: Invalid Date Format, Try -d DD/MM/YYYY')
        sys.exit()

    mon = calendar.month_abbr[int(day.month)]
    dmy = (f"{day.day}" + mon + f"{day.year}")


if dmy[1].isalpha():
    dmy = dmy.zfill(9)
else:
    pass


def ftpfile(dmy):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')
    path = '/Common/NTNEAT'
    ftp.cwd(path)
    try:
        key = 'FTPFILES'
        dir = os.getenv(key) + "/"
        # dir = "/home/nithin/datatCollect/trimData/test/src/script/folder/"
        try:
            fName = [
                "contract.gz_" + dmy,
                "nnf_participant.gz_" + dmy,
                "nnf_security.gz_" + dmy,
                "participant.gz_" + dmy,
                "security.gz",
                "spd_contract.gz",
                     ]
            for i in fName:
                pathDir = dir + i
                ftp.retrbinary("RETR " + i, open(pathDir, 'wb').write)
            
                with open(pathDir, 'rb') as f_in:
                    with gzip.open(pathDir+ '.txt', 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
            ftp.close()

        except:
            print("Error: File not found for particular date in FTP")
            return "null"
            
    except:
        print("Error: path location had not prefered")
        print("run 'sudo gedit /etc/environment' and set 'FTPFILES = *desired directory*'")
        sys.exit() 


check = ftpfile(dmy)
if check != "null":
    print("Downloaded and extracted!...")

