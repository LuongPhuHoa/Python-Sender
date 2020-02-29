import string
import email.message
from time import strftime
import sys
from random import *
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,os,random,time
from colorama import *
from datetime import datetime
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

init()


la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'



def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [ 36]

    x = """
================================Mr Spy S3ndR v0.1============================================
        _____               [+] Facebook : https://www.facebook.com/007MrSpy              [+]
    .-,;='';_),-.           [+] Github :https://github.com/MisterSpyx                     [+]
     \_\(),()/_/            [+] Youtube : https://www.youtube.com/user/TheMrSpyders       [+]
       (,___,)              [+] ICQ : 712083179                                           [+]
      ,-/`~`\-,___          [+] Website : T-shop.to                                       [+]
     / /).:.('--._)         [+] Version : 0.1                                             [+]
    {_[ (_,_)               [+] Date : 11/25/2019                                         [+]
        | Y |               [+] Think Twice , Code one                                    [+]
snd    /  |  \              [+] https://www.youtube.com/watch?v=FyqABRfsIQo               [+]
       """ """              
===========================================================================================



"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()


def sendiyaspy(site):
    try:
        Namex = open('Send3r/Name.txt', 'r')
        Name = random.choice(open('Send3r/Name.txt').readlines())
        Name = Name.replace('\n', '').replace('\r', '')
        Namex.close()
        Subjectx = open('Send3r/Subject.txt', 'r')
        Subject = random.choice(open('Send3r/Subject.txt').readlines())
        Subject = Subject.replace('\n', '').replace('\r', '')
        Subjectx.close()
        smtprandom = open('Send3r/Smtps.txt', 'r')
        smtp = random.choice(open('Send3r/Smtps.txt').readlines())
        smtp = smtp.replace('\n', '').replace('\r', '')
        smtprandom.close()
        ur = smtp.rstrip()
        ch = ur.split('\n')[0].split('|')
        serveraddr = ch[0]
        toaddr = site
        fromaddr = ch[2]
        serverport = ch[1]
        SMTP_USER = ch[2]
        SMTP_PASS = ch[3]
        msg = MIMEMultipart()
        msg['Subject'] = Subject + randomString(10)
        msg['From'] = Name
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        server = smtplib.SMTP()
        server.connect(serveraddr, serverport)
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(fromaddr, [msg['To']], msg.as_string())
        server.quit()
        print  la5dhar + '--------------------------------------MrSpy-S3nder--------------------------------------' + labyadh
        print  labyadh + 'Time 		:' + la7mar + current_time + labyadh
        print  lasfar + 'To 		:' + la7mar + toaddr + labyadh
        print  lasfar + 'Subject 	:' + la7mar + Subject + labyadh
        print  lasfar + 'Name 		:' + la7mar + Name + labyadh
        print  lasfar + 'Smtp 		:' + la7mar + ur + labyadh
        print  lasfar + 'Status 	        :' + la5dhar + 'Success' + labyadh
        print  la5dhar + '--------------------+-------------------------------------------------------------------' + labyadh
    except:
        print  la7mar + '--------------------+-------------------------------------------------------------------' + labyadh
        print '----Smtp Not Wokring I will Delete It -->'+ur
        print  la7mar + '--------------------+-------------------------------------------------------------------' + labyadh

with open('Send3r/letter.txt', 'r') as myfile:
	data = myfile.read()

Email = raw_input('Enter Emails.txt :')



def main():

    for i in ListPass:
        try:
            site = i.strip()
            data=sendiyaspy(site)
        except:
            pass

ListPass = open(Email, 'r').readlines()
pool = ThreadPool(10)
pool.map(sendiyaspy, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success")
