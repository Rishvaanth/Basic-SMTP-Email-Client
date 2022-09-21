import socket

HOST = socket.gethostbyname(
    socket.gethostname())  # gets host machine IP Address. WILL NOT WORK FOR VIRTUAL BOX SYSTEMS.

PORT = 9392

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM IS TCP. AF_INET is IPv4

sender.bind((HOST, PORT))
