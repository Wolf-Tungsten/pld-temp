import schedule
import time


bupload = True
bcheck = True

def upload():
    global bupload
    bupload = True

def check():
    global bcheck
    bcheck = True
 
schedule.every(3).seconds.do(upload)
schedule.every(1).seconds.do(check)
 
while True:
    schedule.run_pending()
    if bupload:
        print("upload image")
        bupload = False
    if bcheck:
        print("check status")
        bcheck = False