import requests, uuid, secrets
import maskpass
import sys,os
import time
import progressbar
import time
from colorama import init
from termcolor import colored
init()
import urllib.request
from colorama import Fore, Back, Style
from time import sleep
os.system('cls')  



# Function to create
def animated_marker():
	
	widgets = ['Loading: ', progressbar.AnimatedMarker()]
	bar = progressbar.ProgressBar(widgets=widgets).start()
	
	for i in range(50):
		time.sleep(0.1)
		bar.update(i)
		
# Driver's code
animated_marker()
os.system('cls')
print('''
      \033[91m██\033[93m╗\033[91m ██████\033[93m╗ \033[91m███████\033[93m╗\033[91m ██████\033[93m╗ \033[91m██████\033[93m╗ 
      \033[91m██\033[93m║\033[91m██\033[93m╔════╝ \033[91m██\033[93m╔════╝\033[91m██\033[93m╔═\033[91m████\033[93m╗╚════\033[91m██\033[93m╗
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m  ███\033[93m╗\033[91m███████\033[93m╗\033[91m██\033[93m║\033[91m██\033[93m╔\033[91m██\033[93m║ \033[91m█████\033[93m╔╝
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m   ██\033[93m║╚════\033[91m██\033[93m║\033[91m████\033[93m╔╝\033[91m██\033[93m║\033[91m██\033[93m╔═══╝ 
      \033[91m██\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m╗
      \033[93m╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝''')     


#FETCHING USERNAME FILES
image_url = "https://raw.githubusercontent.com/Shummi98/don-t_touch/main/userinfo.txt"
r = requests.get(image_url) # create HTTP response object
with open("userinfo.txt",'wb') as f:
    f.write(r.content)
    
    
#FETCHING PASSWORD FILES
image_url = "https://raw.githubusercontent.com/Shummi98/don-t_touch/main/userpassword.txt"
r = requests.get(image_url) # create HTTP response object
with open("userpassword.txt",'wb') as f:
    f.write(r.content)    

#MATCHING USERNAME AND PASSWORD FROM FILES 
inFile = open('userinfo.txt', 'r')
password = inFile.read()
userguess = input("Enter your linked mail: ")
if password == userguess:
    print('')
else:
    print('Mail not registered in IG502')
    exit()
    
    
    
# inFile = open('usertest.txt', 'r')
# username = inFile.read()
inFile = open('userpassword.txt', 'r')
password = inFile.read()
# username = input("Enter username: ")
userguess = input("Enter password: ")
# if username == username:
if password == userguess:
    print('')
else:
    print('Sorry it seem like you have not taken the subscription please contact to admin')
    exit()
os.system('cls')  
input("press enter to continue")
os.system('cls') 


os.system("usertest.txt")                
print('''
      \033[91m██\033[93m╗\033[91m ██████\033[93m╗ \033[91m███████\033[93m╗\033[91m ██████\033[93m╗ \033[91m██████\033[93m╗ 
      \033[91m██\033[93m║\033[91m██\033[93m╔════╝ \033[91m██\033[93m╔════╝\033[91m██\033[93m╔═\033[91m████\033[93m╗╚════\033[91m██\033[93m╗
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m  ███\033[93m╗\033[91m███████\033[93m╗\033[91m██\033[93m║\033[91m██\033[93m╔\033[91m██\033[93m║ \033[91m█████\033[93m╔╝
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m   ██\033[93m║╚════\033[91m██\033[93m║\033[91m████\033[93m╔╝\033[91m██\033[93m║\033[91m██\033[93m╔═══╝ 
      \033[91m██\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m╗
      \033[93m╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝''')     


# os.remove("info.txt")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)



slowprint (''' \033[40m
  +-----------------------------------------+
  | IG502- Instagram mass reporting bot     |       
  +-----------------------------------------+
  | Thanks for taking our subscription      |
  +-----------------------------------------+
  | Coded By GUCCIFER SHUBHAM 2022-Addition |
  +-----------------------------------------+
''')


uid = uuid.uuid4()

r = requests.Session()

cookie = secrets.token_hex(8) * 2

username = input("\033[97m    please enter the bot username:")


password = maskpass.askpass(prompt="\033[97m    please enter the password:" , mask="*")

target = input("\033[97m    please enter the victim username:")

sle = int(input("\033[97m    Enter the delay for reporting(second):"))

print("""\033[91m[1] = spam
[2] = self injury
[3] = hate speech or symbols
[4] =harsement or bulying
[5] = sale or drugs
[6] = violance
[7] = Nudity or pornography
[8] = me ( impreion)""")


mode = input("\033[94mInput the choice:")

def spam():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

                    

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 1, "frx_context": ""}  # spam

            report = r.post(url_report, data=datas)

            print(" \033[40mSucessfully Reported by IG502".format(done))
            

            sleep(sle)

            done += 1
            if done == 150:
                    sys.exit("very high trafic try again in few hours")
            



def self():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]
        done = 1
      


        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 2, "frx_context": ""}  # self

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                      sys.exit("very high trafic try again in few hours")



def hate():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 6, "frx_context": ""}  # hate

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                    sys.exit("very high trafic try again in few hours")
            



def harsement():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1


        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 7, "frx_context": ""}  # harsement

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                    sys.exit("very high trafic try again in few hours")




def Ssleorpromotiondrugs():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1


        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 3,

                "frx_context": "",

            }  # Ssleorpromotiondrugs

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                sys.exit("very high trafic try again in few hours")            



def Violenceorthreatofviolence():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1
       

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 5,

                "frx_context": "",

            }  # Violenceorthreatofviolence

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(0.1)

            done += 1
            if done == 150:
                sys.exit("very high trafic try again in few hours")



def Nudityorpornography():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1
       
        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 4,

                "frx_context": "",

            }  # Nudityorpornography

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                sys.exit("very high trafic try again in few hours")



def mex():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login sucessfull")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1
        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 8, "frx_context": ""}  # me

            report = r.post(url_report, data=datas)

            print("\033[40mSucessfully Reported by IG502".format(done))

            sleep(sle)

            done += 1
            if done == 150:
                sys.exit("very high trafic try again in few hours")

            # done += 1
            # if done == 150:
            #     os.system('rm usertest.txt')
            #     os.system('rm passwordtest.txt')
            #     sys.exit("very high trafic try again in few hours")

    else:

      print("login false")

    exit()



if mode == "1":

    spam()

if mode == "2":

    self()

if mode == "3":

    hate()

if mode == "4":

    harsement()

if mode == "5":

    Ssleorpromotiondrugs()

if mode == "6":

    Violenceorthreatofviolence()

if mode == "7":

    Nudityorpornography()

if mode == "8":

    mex()

os.system('rm usertest.txt')
os.system('rm passwordtest.txt')
