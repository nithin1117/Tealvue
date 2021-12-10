from ftplib import FTP
from datetime import date

today = date.today()
mon = today.strftime("%b").upper()
DMY = today.strftime("%d"+ mon +"%Y")


ftp = FTP('ftp.connect2nse.com')
ftp.login('FTPGUEST', 'FTPGUEST')


path = '/Common/NTNEAT'
ftp.cwd(path)

# fileName1 = "contract.gz_"+DMY
fileName1 = "contract.gz_23Nov2021"
fileName2 = "nnf_participant.gz_23Nov2021"
fileName3 = "nnf_security.gz_23Nov2021"
fileName4 = "participant.gz_23Nov2021"
fileName5 = "security.gz"
fileName6 = "spd_contract.gz"

#dir = input()
#change directory according to your preferences
dir = "/home/nithin/Documents"

ftp.retrbinary("RETR " + fileName1, open(dir + fileName1, 'wb').write)
ftp.retrbinary("RETR " + fileName2, open(dir + fileName2, 'wb').write)
ftp.retrbinary("RETR " + fileName3, open(dir + fileName3, 'wb').write)
ftp.retrbinary("RETR " + fileName4, open(dir + fileName4, 'wb').write)
ftp.retrbinary("RETR " + fileName5, open(dir + fileName5, 'wb').write)
ftp.retrbinary("RETR " + fileName6, open(dir + fileName6, 'wb').write)


ftp.close()
print("Downloaded")
