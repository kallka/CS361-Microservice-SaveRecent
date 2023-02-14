# Author: Karina Kallas
# Project: Assignment 8 - Microservice for Partner
# Description: Saves recent conversions for unit converter. example_ui.py shows how to interact with
#               client_handler.py if the program imports client_handler


# import random only needed for example UI.
import random
import time
# ----------------------------------------------------------------------------------------
#
#                   COMMON MESSAGES
#
# ----------------------------------------------------------------------------------------
"""
- Saved messages for communication
- Saved variables that can be changed by client.
"""
disconnect_msg = "quit"
receive_msg = "send"

# ---------------------------------------------------------
#
#       HOW TO:
#           Examples of how to save to text files in UI for communication with client handler.
#           Interact with client_handler.py by saving message in .txt file
#
# ---------------------------------------------------------


def save_conversion(return_conversion):
    """
    Sends a recent conversion. Here saved as return_conversion.
    Scroll down to see this within the example Client UI.
            params: a recent conversion
            returns: no return will be received
    """
    file_write = open("message.txt", "w")
    file_write.write(return_conversion)
    file_write.close()


def see_recent():
    """
    Requests recent searches from client_handler.
    Scroll down to see this within the example Client UI.
            params: none needed
            returns: will return a list of recent conversions
    """
    file_write = open("message.txt", "w")
    file_write.write(receive_msg)
    file_write.close()
    time.sleep(1.0)

    file_read = open("recent-search.txt", "r")
    line = file_read.readline()
    file_read.close()

    print(line)


def disconnect():
    """
    Sends a recent conversion. Here saved as return_conversion.
    Scroll down to see this within the example Client UI.
            params: a recent conversion
            returns: no return will be received
    """
    file_write = open("message.txt", "w")
    file_write.write(disconnect_msg)
    file_write.close()

# -------------------------------------------------------------------------------------------------
#
#       HOW TO:
#
#       An example client-side UI.  Includes possible placement for:
#                                                   - example_send_recent_conversion()
#                                                   - example_see_recent_searches()
#
# -------------------------------------------------------------------------------------------------
def example_conversion(unit1):
    """
    Example function - does not convert any units.
    Demonstrates how to send recent conversion to client_handler.
    """
    # Example list to use for example client UI.
    ex_list = ["1 inch = 2.540 centimeters",
               "1 sq. inch = 6.4516 sq. centimeters",
               "1 grain = 0.05 scruples",
               "1 teaspoon = 5 milliliters",
               "1 sq. yard = 0.83613 sq. meters"''
               ]
    # Fake conversion:
    return_conversion = random.choice(ex_list)              # Randomly select conversion for example purposes
    print(f"What you entered: {unit1}")                     # Example print to screen
    print(f"Your fake conversion: {return_conversion}")     # Example print to screen

    save_conversion(return_conversion)       # Send to client_handler to save at server.


def example_ui():
    """
        A basic example client-side UI.
    """
    connected = True
    while connected:
        unit1 = input("Enter 'quit' to end program at anytime. \nPlease enter unit for conversion: ")
        if unit1 == "quit":
            disconnect()
            connected = False
        else:
            example_conversion(unit1)

        response = input("Would you like to see your 3 most recent conversions? (Y/N): ")
        if response == "Y":
            see_recent()


example_ui()
