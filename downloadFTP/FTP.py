'''importing necessary stuffs'''
from ftplib import FTP
import gzip
import shutil


# '''To execute in current date'''
# from datetime import date
# today = date.today()
# mon = today.strftime("%b")
# DMY = today.strftime("%d" + mon + "%Y")


'''To execute in specific date'''
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




ftp = FTP('ftp.connect2nse.com')
ftp.login('FTPGUEST', 'FTPGUEST')

path = '/Common/NTNEAT'
ftp.cwd(path)

fileName1 = "contract.gz_"+DMY
fileName2 = "nnf_participant.gz_"+DMY
fileName3 = "nnf_security.gz_"+DMY
fileName4 = "participant.gz_"+DMY
fileName5 = "security.gz"
fileName6 = "spd_contract.gz"

try:
    dir = input("Enter path(with / in front and back):")
#    dir = "/home/nithin/Documents/sample/new/"


    ftp.retrbinary("RETR " + fileName2, open(dir + fileName2[:18], 'wb').write)
    ftp.retrbinary("RETR " + fileName3, open(dir + fileName3[:15], 'wb').write)
    ftp.retrbinary("RETR " + fileName4, open(dir + fileName4[:14], 'wb').write)
    ftp.retrbinary("RETR " + fileName5, open(dir + fileName5, 'wb').write)
    ftp.retrbinary("RETR " + fileName6, open(dir + fileName6, 'wb').write)
    ftp.retrbinary("RETR " + fileName1, open(dir + fileName1[:11], 'wb').write)

    ftp.close()
    print("Downloaded")

    with open('/home/nithin/Documents/sample/new/contract.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/contract' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('/home/nithin/Documents/sample/new/nnf_participant.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/nnf_participant' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('/home/nithin/Documents/sample/new/nnf_security.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/nnf_security' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('/home/nithin/Documents/sample/new/participant.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/participant' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('/home/nithin/Documents/sample/new/security.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/security' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    with open('/home/nithin/Documents/sample/new/spd_contract.gz', 'rb') as f_in:
        with gzip.open('/home/nithin/Documents/sample/new/extracted/spd_contract' + DMY + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            


    print("Extracted!!!...")
   

except:
    print("Either File not Found or Path directory Error")

