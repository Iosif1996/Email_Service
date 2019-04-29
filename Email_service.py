import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests

recipients = []

def todaysNews():
    source = requests.get('https://www.theguardian.com/world').text

    soup = BeautifulSoup(source, 'lxml')

    news = soup.find('div', class_='fc-container--rolled-up-hide')

    return news

def addSubs(numOfSubs):
    
    for i in range(numOfSubs):
        print('Enter the subscribers that you wish to add here!: ')
        recipients.append(input())

    return print('New Subscribers: ',recipients)

def removeSubs(numOfSubs):
    for i in range(numOfSubs):
        print('Enter the subscribers that you wish to remove here: ')
        recipients.remove(input())
    return print('Current subscribers list ',recipients)

def emailService():
    try:
        email_user = 'emailservicetest69@gmail.com'

        subject = " Today's  world news"

        msg = MIMEMultipart()

        msg['From'] = email_user
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        body = todaysNews()
        msg.attach(MIMEText(body,'html'))
        text = msg.as_string()
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,'Test2019,')

        server.sendmail(email_user, recipients ,text)

        server.quit()
        print('Email have been succesfully send!!')
    except:
        print('You probably typed an invalid email or there is an issue with the servers.. \nEmail failed to be send!!!')
    


subNum=int(input("Enter the number of subscribers that you want to send email to: "))
addSubs(subNum)

print("We can't continue if we don't confirm that everything is alright")
print("Do you want to proceed? y/n")
proceed = input()

if (proceed.lower()) == 'n':
    print('Your current list of subscribers: ',recipients)
    print("Do you want to 'add' or 'remove' a subscriber?")
    decision = input()
    if (decision.lower()) == 'add':
        numExtraAdd = int(input("How many subscribers you wish to add? "))
        addSubs(numExtraAdd)
        emailService()

    elif (decision.lower()) == 'remove':
        numRemoveSubs = int(input("How many subscribers you wish to remove? "))
        removeSubs(numRemoveSubs)
        emailService()

    elif (decision.lower()) != 'add' or 'remove':
        print("ERROR!! \n We offer only two functions please choose one of them and be careful of spelling!! \n Re-run the program please!!")

elif (proceed.lower()) == 'y':
    print('Sending email to: ', recipients)
    emailService()

elif (proceed.lower()) != 'y' or 'n':
    print("ERROR!!\n Sorry you probably typed another character instead of 'y' or 'n'!! \n Re-run the program please!!")


