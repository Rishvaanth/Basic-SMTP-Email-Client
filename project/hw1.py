import subprocess
import sys
import re
from socket import *

content = subprocess.run(['cat', f'{sys.argv[1]}']
                         , capture_output=True
                         , text=True)  # Taking the argument as text input

if content.returncode != 0:  # file has been found
    print("\n")
    print("The script has failed. Reason: "f'{content.stderr}')

else:
    print("\n")
    mail = content.stdout
    print(f'File with content has been found.. \n\nThe mail to be sent... \n\n{mail}')

    context = open(sys.argv[1], "r")
    parsings = context.readlines()

    for sender in parsings:
        senderText = sender
        if sender.find("From") != -1:
            parsings.remove(sender)
            break
    else:
        print(f'Please check the input file {context.name} for proper Sender format')
        sys.exit("Unable to find sender address in the file. Exiting the process.")
    senderEmail = senderText[senderText.rfind('<') + 1:senderText.rfind('>')]

    for receiver in parsings:
        receiverText = receiver
        if receiver.find("To") != -1:
            parsings.remove(receiver)
            break
    else:
        print(f'Please check the input file {context.name} for proper Receiver format')
        sys.exit("Unable to find the receiver address in the file. Exiting the process.")
    receiverEmail = receiverText[receiverText.rfind('<') + 1:receiverText.rfind('>')]

    for subject in parsings:
        subjectText = subject
        if subject.find("Subject") != -1:
            parsings.remove(subject)
            break

    else:
        print(f'Please check the input file {context.name} for proper Subject format')
        sys.exit("Unable to find the mail subject in the file. Exiting the process.")

    subject = f"{subject} \r\n\r\n"

    messageBody = parsings.pop()
    print(f"The message body is {messageBody}")
    messageBody = f"\r\n {messageBody}"

    receiverDomain = receiverEmail[receiverEmail.rfind("@") + 1:]
    hostAddress = subprocess.run(["host", "-t", "mx", f"{receiverDomain}"]
                                 , capture_output=True
                                 , text=True)  # extracting the server address of the receiver

    if hostAddress.returncode != 0:
        sys.exit(f"Receiver Server Domain not resolved. Reason: {hostAddress.stderr}\nPlease check the domain info\n")

    print(f'The mail server is:{receiverDomain} \n')
    hostAddress = hostAddress.stdout
    hostAddress = hostAddress[hostAddress.rfind('by') + 2:].strip()
    serverAddress = re.sub("[0-9]", "", hostAddress)  # removing numeric value from the mail server address
    serverAddress = re.sub(" ", "", serverAddress)  # removing blank spaces
    print(f'The server address is {serverAddress}')

    clientSocket = socket(AF_INET, SOCK_STREAM)
    emailServer = (serverAddress, 25)
    clientSocket.connect(emailServer)
    messageTerminator = "\r\n.\r\n"
    resp1 = clientSocket.recv(1024)
    resp1 = resp1.decode()
    print(f"Connection Request - Response:{resp1}")
    if resp1[:3] != "220":  # Checking for 220 code in response.
        print(f"220 response not found from server {emailServer}")
    ehlo = "EHLO Alice\r\n"
    clientSocket.send(ehlo.encode())
    resp2 = clientSocket.recv(1024)
    resp2 = resp2.decode()
    print(f'Response for EHLO command: {resp2}')
    if resp2[:3] != '250':
        sys.exit('250 response not received from the server after EHLO. Exiting the execution.')
    print(f"The sender email is: {senderEmail}")
    mailFrom = f"MAIL FROM:<{senderEmail}>\r\n"
    clientSocket.send(mailFrom.encode())
    resp3 = clientSocket.recv(1024)
    resp3 = resp3.decode()
    print("Response after \"MAIL FROM\" command:" + resp3)
    mailTo = f"RCPT TO:<{receiverEmail}>\r\n"
    clientSocket.send(mailTo.encode())
    resp4 = clientSocket.recv(1024)
    resp4 = resp4.decode()
    print(f"After RCPT TO command: {resp4}")
    if resp4[:3] != '250':
        sys.exit('250 response not received from the server after RCPT command. Error message is visible above this '
                 'statement. exiting the program.')
    dataSegment = "DATA\r\n"
    clientSocket.send(dataSegment.encode())
    resp5 = clientSocket.recv(1024)
    resp5 = resp5.decode()
    print(f"After DATA command:{resp5}")
    clientSocket.send(subject.encode())
    clientSocket.send(messageBody.encode())
    clientSocket.send(messageTerminator.encode())
    resp6 = clientSocket.recv(1024)
    print(f"Response after the message contents:{resp6.decode()}")
    quitComms = "QUIT\r\n"
    clientSocket.send(quitComms.encode())
    resp6 = clientSocket.recv(1024)
    print(resp6.decode())
    clientSocket.close()

