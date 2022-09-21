import subprocess
import sys
import smtplib

content = subprocess.run(['cat', f'{sys.argv[1]}']
                         , capture_output=True
                         , text=True)  # Taking the argument as text input

if content.returncode == 0:  # file has been found
    print("\n")
    mail = content.stdout
    print(f'File with content has been found.. \n\nThe mail to be sent... \n\n{mail}')

    context = open(sys.argv[1], "r")
    parsings = context.readlines()

    for sender in parsings:
        senderText = sender
        if sender.find("From") != -1:
            break
    else:
        print(f'Please check the input file {context.name} for proper Sender format')
    # TODO Create an exception at the warning if senderText has not been assigned.
    senderEmail = senderText[senderText.rfind('<') + 1:senderText.rfind('>')]

    for receiver in parsings:
        receiverText = receiver
        if receiver.find("To") != -1:
            break
    else:
        print(f'Please check the input file {context.name} for proper Receiver format')
    # TODO Create an exception at the warning if receiverText has not been assigned.
    receiverEmail = receiverText[receiverText.rfind('<') + 1:receiverText.rfind('>')]

    receiverDomain = receiverEmail[receiverEmail.rfind("@") + 1:]

    hostAddress = subprocess.run([f'"host", "-t", "mx", "{receiverDomain}"'],)

    try:
        s = smtplib.SMTP('mail.getnada.com', 25)
        s.sendmail(f'{senderEmail}', f'{receiverEmail}', content.stdout)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")

else:
    print("\n")
    print("The script has failed. Reason: "f'{content.stderr}')
