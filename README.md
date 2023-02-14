# CS361-Microservice-SaveRecent
# Description: Saves recent input from a client UI. For my partner's project, it will save recent unit conversions.

HOW TO SET UP


IMPORTANT RULES PRIOR TO SET UP:

1.) Please use the example_ui.py for help. 

2.) Important Items:

      a.) save_recent() - needs to be connected to a return of "recent conversion"
      b.) see_recent()
      c.) disconnect()
      
3.) Needed variables:

      a.) disconnect_msg = "quit"
      b.) receive_msg = "send"
      
4.) The UI can be implemented to fit your program but 2.a - 2.c need to be implemented in order for the microservice to function.


IMPLEMENTATION AND HOW IT WORKS:

1.) Variable - disconnect_msg = "quit"

      - This is the exact message needed to send a disconnect message to client_hanlder (which in turn sends it to server). 
      
      - The message needs to be saved in the "message.txt" file.
      
2.) Variable - receive_msg = "send"

      - This is the exact message needed to retrieve the queue of saved conversions (3 exactly - but number can be changed in server.py)
      
      - This message is saved in the "message.txt" file.
      
3.) Function - save_recent():

      - Params: the most recent conversion sent to the client (as a string)
      
      - sends to client_handler
      
      - client_handler determines that it is a message to be saved and sends to server.py
      
      - server.py saves it to the queue and if necessary dequeues the first item in the queue to maintain a max of 3 items in recent queue
      
4.) Function - see_recent():

      - Params: receive_msg = "send"
      - sends the receive_msg to the client_handler.py
      - client_handler sends the message to server.py and receives a message back (the most recent saves in the queue)
      - client_handler changes this message to a string and saves it to "recent-searches.txt"
      - see_recent() reads "recent_searches.txt" and prints the queue to the terminal
5.) Function - disconnect():

      - copies the disconnect_message = "quit" to "message.txt"
      - client_handler.py reads the message, forwards to the server, and then quits

UML: Please download from the link:
[CS361_Assignment8_UML.pdf](https://github.com/kallka/CS361-Microservice-SaveRecent/files/10729370/CS361_Assignment8_UML.pdf)
