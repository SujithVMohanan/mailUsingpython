import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('sender@gmail.com', 'password')   # google accounts less secure apps must allow
server.sendmail('sender@gmail.com', 'reciever@gmail.com', 'message')
server.quit()