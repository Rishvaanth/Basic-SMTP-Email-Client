import socket
import subprocess
import smtplib

msg = """From: "Hamed" <test@uwm.edu>
To: "hamed" <hamed.rezaei@zoho.com>
Subject: testing

Compsci520 is a cool course!!"""

try:
    s = smtplib.SMTP('mail.getnada.com', 25)
    s.sendmail('test@uwm.edu', 'fuqosa@getnada.com', msg)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")

# RECV_SERVER = 'mail.getnada.com'
#
# # HOST = 'daring.cwi.nl'    # The remote host
# # The same port as used by the server
# subject = 'Test email'
# body = 'Test Test lorem ipsum scandalum balhniufeiubwef'
# msg = f'Subject: {subject}\n\n{body}'
# msg = msg.encode()
# print(msg)
#
# # TCP_IP = '127.0.0.1'
# # TCP_PORT = 5005
# BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!"
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((RECV_SERVER, 25))
# s.send(MESSAGE)
# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #     s.connect((RECV_SERVER, 25))
# #     s.sendmsg(msg)
#
# # with smtplib.SMTP(RECV_SERVER, 25) as smtp:
# #     smtp.ehlo()
# #     # smtp.starttls()
# #     # smtp.ehlo()
# #
# #     # smtp.login('candyman@getnada.com', 'test')
# #
# #     smtp.sendmail('candyman@getnada.com', 'fuqosa@getnada.com', msg)
