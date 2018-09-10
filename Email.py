import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
password = input('Enter Password: ')
smtpObj.login(' pjconnolly12@gmail.com ', password )
smtpObj.sendmail(' pjconnolly12@gmail.com ', ' pjconnolly12@gmail.com ', 'Subject: Test Email\nHey Pat this is a test')
smtpObj.quit()

