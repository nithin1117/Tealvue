import ftplib
from datetime import date


today = date.today()
mon = today.strftime("%b").upper()
DMY = today.strftime("%d" + mon + "%y")


path = '/Common/NTNEAT'

# fileName = "contract.gz_"+DMY
fileName1 = "contract.gz_23Nov2021"
fileName2 = "nnf_participant.gz_23Nov2021"
fileName3 = "nnf_security.gz_23Nov2021"
fileName4 = "participant.gz_23Nov2021"
fileName5 = "security.gz"
fileName6 = "spd_contract.gz"


ftp = ftplib.FTP('ftp.connect2nse.com')
ftp.login('FTPGUEST', 'FTPGUEST')
ftp.cwd(path)

# ftp.retrlines("LIST")

ftp.retrbinary("RETR " + fileName1, open(fileName1, 'wb').write)
ftp.retrbinary("RETR " + fileName2, open(fileName2, 'wb').write)
ftp.retrbinary("RETR " + fileName3, open(fileName3, 'wb').write)
ftp.retrbinary("RETR " + fileName4, open(fileName4, 'wb').write)
ftp.retrbinary("RETR " + fileName5, open(fileName5, 'wb').write)
ftp.retrbinary("RETR " + fileName6, open(fileName6, 'wb').write)


ftp.quit()
