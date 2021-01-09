import time
import smtplib, ssl
from os import system, name
from colorama import Fore, Back, Style
import sys
from tqdm import tqdm


def clear():
    if name == 'nt':
        _ = system('cls')

print(Fore.GREEN + "This tool was made by Jam")
print(Fore.RED + '''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(
 `------'
 Server:https://discord.gg/Rkneqm4uZN
 To work turn on less secure app access
 !The mail may appear in spam folder!
''')
time.sleep(1)
print("Btw i made this apart from some code before getting mad")
clear()
time.sleep(0.1)
print("Loading...")
time.sleep(5)
clear()
print(Fore.RED + '''
Email spammer made by Jam
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(
 `------'
''')
smtp_server = "smtp.gmail.com"
port = 587
sender_email = input("Enter Email:")
password = input("Enter password:")
receiver_email = input("Enter victim:")
message = input("Enter message:")
times = input("Enter ammount of times:")
times1 = int(times)
context = ssl.create_default_context()

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    for times1 in range(times1):
        server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
    time.sleep(10)
    server.quit()
finally:
    print("Finished...")
    time.sleep(1)
    server.quit()
