# Author: Karina Kallas
# Project: Assignment 8 - Microservice for Partner
# Description: Saves recent conversions for unit converter.
#               server.py handles messages from client_handler, saves recent searches,
#               and returns recent searches.

# ----------------------------------------------------------------------------------------
#
#                   IMPORTS
#
# ----------------------------------------------------------------------------------------
import socket
import threading
from collections import deque


# ----------------------------------------------------------------------------------------
#
#                   CONNECTION INFORMATION
#
# ----------------------------------------------------------------------------------------
"""
- Header allows to limit size of bytes being recieved.
- gethostbyname() will automatically connect to local.
"""
HEADER = 64     # BYTES
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


# ----------------------------------------------------------------------------------------
#
#                   MESSAGES, COMMON VARIABLES, AND SAVED QUEUE (saved_q)
#
# ----------------------------------------------------------------------------------------
"""
- Saved messages for communication
- Saved variables that can be changed by client.
"""
start_msg = "Server is starting...."
disconnect_msg = "quit"
receive_msg = "send"
empty = "empty"
num = 3
saved_q = deque()


# ----------------------------------------------------------------------------------------
#
#                   SERVER SET UP WITH SOCKET
#
# ----------------------------------------------------------------------------------------
"""
Bind to local host.
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# ----------------------------------------------------------------------------------------
#
#                   HANDLE CLIENT
#
# ----------------------------------------------------------------------------------------
def handle_client(conn, addr):
    # alerts to new client connection
    print(f"NEW CONNECTION: {addr} connected.")

    connected = True
    while connected:
        # set up for reading message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # please use this for clean disconnect to avoid error messages
            if msg == disconnect_msg:
                print(f"Quit request received:", disconnect_msg)
                msg = empty
                message = msg.encode(FORMAT)
                conn.send(message)
                connected = False

            # client used "receive" and wants saved searches returned
            if msg == receive_msg:
                msg = ""
                for item in saved_q:
                    msg += f" {item},"
                message = msg.encode(FORMAT)
                conn.send(message)

            # client has sent a recent conversion to save
            else:
                #
                print(msg)
                saved_q.append(msg)
                print("current queue:", saved_q)
                if len(saved_q) > num:
                    saved_q.popleft()
                    print("dequeued:", saved_q)
                msg = empty
                message = msg.encode(FORMAT)
                conn.send(message)

            # can be removed - for server side only
            print(f"We have received and processed the following message: \n {msg}")

    conn.close()


# ----------------------------------------------------------------------------------------
#
#                   START: LISTEN AND THREAD
#
# ----------------------------------------------------------------------------------------
def start():
    server.listen()
    print(f"Server is listening on: {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # This prints how many client connections.
        # Minus 1 from active threads for this server start thread.
        print(f"ACTIVE CONNECTIONS: {threading.activeCount()-1}")


# ----------------------------------------------------------------------------------------
#
#                   START MESSAGE / CALL START FUNCTION
#
# ----------------------------------------------------------------------------------------
print(start_msg)
start()