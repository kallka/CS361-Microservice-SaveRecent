# Author: Karina Kallas
# Project: Assignment 8 - Microservice for Partner
# Description: Saves recent conversions for unit converter.
#               client_handler.py handles messages to server from client, functions designed to be called
#               by importing client_handler, if necessary.

# ----------------------------------------------------------------------------------------
#
#                   IMPORTS
#
# ----------------------------------------------------------------------------------------
import socket
import time

# ----------------------------------------------------------------------------------------
#
#                   CONNECTION INFORMATION
#
# ----------------------------------------------------------------------------------------
HEADER = 64     # BYTES
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


# ----------------------------------------------------------------------------------------
#
#                   CLIENT SET UP WITH SOCKET
#
# ----------------------------------------------------------------------------------------
"""
Bind to local host.
"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# ----------------------------------------------------------------------------------------
#
#                   COMMON MESSAGES
#
# ----------------------------------------------------------------------------------------
"""
- Saved messages for communication
- Saved variables that can be changed by client.
"""
start_msg = "Client is starting...."
disconnect_msg = "quit"
receive_msg = "send"
empty = "empty"


# ----------------------------------------------------------------------------------------
#
#                   SEND AND RECEIVE MESSAGES
#
# ----------------------------------------------------------------------------------------
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))   # b' ' is byte representation of space
    client.send(send_length)
    client.send(message)
    recent_saved = client.recv(2048)
    if recent_saved == empty:
        return
    else:
        return recent_saved


def get_saved(msg):
    msg = receive_msg
    recent_saved = str(send(msg))
    print("First received,", recent_saved)
    recent_saved = recent_saved[2:-2]
    print("edit", recent_saved)

    file_write = open("recent-search.txt", "w")
    file_write.write(str(recent_saved))
    file_write.close()


connected = True
while connected:
    time.sleep(0.5)
    # new message can also take a direct input()
    file_read = open("message.txt", "r")
    new_message = file_read.readline()
    file_read.close()

    file_write = open("message.txt", "w")
    file_write.write("")
    file_write.close()

    if len(new_message) > 1:
        print("got the message to client_handler", new_message)
        if new_message == disconnect_msg:
            send(new_message)
            connected = False
        if new_message == receive_msg:
            get_saved(new_message)
        else:
            send(new_message)
