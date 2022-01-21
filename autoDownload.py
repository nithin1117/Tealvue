from datetime import date
import datetime
from zipfile import ZipFile
from urllib.request import urlretrieve as retrieve
import schedule
import time

''' packages tha has to be installed before running this code '''
# pip install urllib3
# pip install datetime
# pip install APScheduler

'''change your desired path in the line number: 23
 change the auto download time in the line number: 46 '''


def downloadFiles():
    tdy = date.today().strftime("%d%m%Y")
    date1 = date.today().strftime("%d")
    year = date.today().strftime("%Y")
    mon = date.today().strftime("%b").upper()

    dmy = date1 + mon + year
    # # enter your path directory here
    path_dir = "D:/New2/"

    if datetime.datetime.today().weekday() < 5:
        url_oi = "https://archives.nseindia.com/content/nsccl/fao_participant_oi_" + tdy + ".csv"
        url_vol = "https://archives.nseindia.com/content/nsccl/fao_participant_vol_" + tdy + ".csv"
        url_ban = "https://archives.nseindia.com/archives/fo/sec_ban/fo_secban_" + tdy + ".csv"
        url_cmvolt = "https://archives.nseindia.com/archives/nsccl/volt/CMVOLT_" + tdy + ".CSV"
        url_combOI = "https://archives.nseindia.com/archives/nsccl/mwpl/combineoi_" + tdy + ".zip"
        url_bhavcopy = "https://www1.nseindia.com/content/historical/EQUITIES/" + year + '/' + mon + "/cm" + dmy + "bhav.csv.zip"

        retrieve(url_oi, path_dir + r"/fao_participant_oi_" + tdy + ".csv")
        retrieve(url_vol, path_dir + r"/fao_participant_vol_" + tdy + ".csv")
        retrieve(url_ban, path_dir + r"/ban" + tdy + ".csv")
        retrieve(url_cmvolt, path_dir + r"/cmvolt" + tdy + ".CSV")
        retrieve(url_combOI, path_dir + r"/combinedOI" + tdy + ".zip")
        retrieve(url_bhavcopy, path_dir + r"cm" + dmy + "bhav.zip")

        file_name = path_dir + 'combinedOI' + tdy + '.zip'
        with ZipFile(file_name, 'r') as zip:
            zip.extractall(path_dir + "/combinedOI" + tdy)

        file_name = path_dir + "cm" + dmy + "bhav.zip"
        with ZipFile(file_name, 'r') as zip:
            zip.extractall(path_dir + "/cm" + dmy + "bhavcopy")
        print(f"download completed for date: {dmy}")

    else:
        print("Today is non-working day")


schedule.every().day.at("21:35").do(downloadFiles)

while True:
    schedule.run_pending()
    time.sleep(1)
