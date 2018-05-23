#References: https://docs.python.org/3/contents.html
#            https://github.com/aslattum/python-tcp-calculator
#            Core Python Application Programming 3rd Edition
#Created by Kevin CHau And Adriam Gonzalez

from math import * #Allows more math functions to be entered
from socket import *		 	 # Import socket module

s = socket() 	  		 # Create a socket object
s.bind((gethostname(), 1200)) 			 # retreive host and bind to the port
s.listen(1) 			         # Now wait for client connection.

print("Server is up and running")

while True:
     c, addr = s.accept() 		# Establish connection with client.
     print('Got connection from', addr)

     while True:
          try:
               #Receiving equation from socket
               equation=c.recv(2048).decode()
               if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
                    c.send("Quit".encode())
                    break
               else:
                    #Displays equation entered
                    print("You gave me the equation:", equation)
                    result = eval(equation)
                    c.send(str(result).encode())
                    #Errors called and calls client side
          except (ZeroDivisionError):
               c.send("ZeroDiv".encode())
          except (ArithmeticError):
               c.send("MathError".encode())
          except (SyntaxError):
               c.send("SyntaxError".encode())
          except (NameError):
               c.send("NameError".encode())

     c.close() 			# Close the connection.
