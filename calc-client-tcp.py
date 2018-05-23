#References: https://docs.python.org/3/contents.html
#            https://github.com/aslattum/python-tcp-calculator
#            Core Python Application Programming 3rd Edition
#Created by Kevin Chau and Adriam Ganzalez

from math import *#Allows nore math functiions to be entered
from socket import *		 	 # Import socket module

s = socket() 	  		 # Create a socket object
s.connect((gethostname(), 1200)) #retrieve host and bind it to port
while(True):
    equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
    s.send(equ.encode())
    result = s.recv(2048).decode('utf-8')
    #End the program
    if result == "Quit":
        print("Closing client connection, goodbye")
        quit();
        #Errors called
    elif result == "ZeroDiv":
        print("ERROR: DIVIDE BY 0")
    elif result == "MathError":
        print("There is an error with your math, try again")
    elif result == "SyntaxError":
        print("There is a syntax error, please try again")
    elif result == "NameError":
        print("You did not enter an equation, try again")
        #Print result
    else:
        print("The answer is:", result)
        s.close  				 # Close the socket when done

