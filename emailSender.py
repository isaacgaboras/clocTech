import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def main():
    prevName = 'test.txt'
    newName = 'CLOC.txt'
    #Name and Password to the account you want to send the email
    userEmail = input("Enter Your Email Address: ")
    passwordEmail = input("Password: ")

    #The email that will receive the data file
    receiveEemail = input("Enter The Email Address You Want To Send It To: ")

    #The subject of the email
    subjectEmail = input("Email Subject: ")

    signal = MIMEMultipart()
    signal['From'] = userEmail
    signal['To'] = receiveEemail
    signal['Subject'] = subjectEmail

    #Write a message to the designated user
    messageEmail = input("Write Message To The Client: ")
    signal.attach(MIMEText(messageEmail, 'plain'))

    #The file that will be sent with the data
    filename = input("Enter the name of the file containing the Data: ")
    attachment = open(filename, 'rb')

    #Sending the attached .txt file with data
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition', "attachment; filename= "+filename)

    signal.attach(part)
    content = signal.as_string()

    #Port to send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(userEmail, passwordEmail)

    server.sendmail(userEmail, receiveEemail, content)
    server.quit()

    print("Email Sent!")


if __name__ == "__main__":
    main()

exit()
