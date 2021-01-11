import time
import smtplib, ssl
from os import system, name
from colorama import Fore, Back, Style
import sys
from tqdm import tqdm
import pyfiglet
import pyautogui

out = pyfiglet.figlet_format("JET", font="doh")
outstand = pyfiglet.figlet_format("Spammer", font="rectangles")
smtp_server = "smtp.gmail.com"
port = 587

def clear(): #this clears screen
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
             Type help for help
''')
startup = input("Press enter to continue:")
if startup == 'help':
    time.sleep(1)
    print('''
     Server:https://discord.gg/Rkneqm4uZN
     To work turn on less secure app access
     !The mail may appear in spam folder!
    ''')
    time.sleep(10)
clear()
print(Fore.BLUE + out)
print("Jams email tool")
print('''
--Gmail tools--
1)Gmail spammer
--Yahoo tools--
2)Yahoo spammer
--Outlook tools--
3)Outlook spammer
(More tools coming soon)
''')
optionfirst = input("Enter option:")

if optionfirst == '1':
    clear()
    print(Fore.BLUE + outstand)
    sender_email = input(Fore.RED + "Enter your email:") #email for you account
    password = input("Enter password:") #password for your account
    receiver_email = input("Enter victim:") #victims email
    message = input("Enter message:") #message
    times = input("Enter ammount of times:") #how many times it sends the email
    times1 = int(times) #changes the string to an int
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        for times1 in range(times1): #this is the loop and loop counter
            server.sendmail(sender_email, receiver_email, message)
            times2 = str(times1)
            print("Emails sent: [" + times2 + "]")
    except Exception as e: #prints the error
        print("Error, sending Exception.. ")
        time.sleep(1)
        print(e)
        time.sleep(10)
        server.quit() #quits
    finally:
        print("")

        print("Finsihed sending all: [" + times2 + "] emails!")
        time.sleep(1)
        server.quit() #quits after all emails have been sent

if optionfirst == '2':
    clear()
    print(Fore.BLUE + outstand)
    sender_email = input(Fore.RED + "Enter your email:") #email for you account
    password = input("Enter password:") #password for your account
    receiver_email = input("Enter victim:") #victims email
    message = input("Enter message:") #message
    times = input("Enter ammount of times:") #how many times it sends the email
    times1 = int(times) #changes the string to an int
    context = ssl.create_default_context()

    try:
        server1 = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server1.ehlo()
        server1.starttls(context=context)
        server1.ehlo()
        server1.login(sender_email, password)
        for times1 in range(times1): #this is the loop and loop counter
            server1.sendmail(sender_email, receiver_email, message)
            times2 = str(times1)
            print("Emails sent: [" + times2 + "]")
    except Exception as e: #prints the error
        print("Error, sending Exception.. ")
        time.sleep(1)
        print(e)
        time.sleep(10)
        serve1r.quit() #quits
    finally:
        print("")

        print("Finsihed sending all: [" + times2 + "] emails!")
        time.sleep(1)
        server1.quit() #quits after all emails have been sent

if optionfirst == '3':
    clear()
    print(Fore.BLUE + outstand)
    sender_email = input(Fore.RED + "Enter your email:") #email for you account
    password = input("Enter password:") #password for your account
    receiver_email = input("Enter victim:") #victims email
    message = input("Enter message:") #message
    times = input("Enter ammount of times:") #how many times it sends the email
    times1 = int(times) #changes the string to an int
    context = ssl.create_default_context()

    try:
        server2 = smtplib.SMTP("smtp.mail.outlook.com", 587)
        server2.ehlo()
        server2.starttls(context=context)
        server2.ehlo()
        server2.login(sender_email, password)
        for times1 in range(times1): #this is the loop and loop counter
            server2.sendmail(sender_email, receiver_email, message)
            times2 = str(times1)
            print("Emails sent: [" + times2 + "]")
    except Exception as e: #prints the error
        print("Error, sending Exception.. ")
        time.sleep(1)
        print(e)
        time.sleep(10)
        server2.quit() #quits
    finally:
        print("")

        print("Finsihed sending all: [" + times2 + "] emails!")
        time.sleep(1)
        server2.quit() #quits after all emails have been sent

