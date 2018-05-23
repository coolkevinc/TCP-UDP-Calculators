#References: https://docs.python.org/3/contents.html
#            https://github.com/aslattum/python-tcp-calculator
#            Core Python Application Programming 3rd Edition
#Created Kevin Chau and Adriam Gonzalez

from math import *
from socket import *

serverName = 'localhost'
serverport = 12000
sock = socket(AF_INET, SOCK_DGRAM)
#equation = input('Enter an equation: ')

#equation,clientAddress = sock.recvfrom(2048)
#answer,clientAddress = sock.recvfrom(2048)
#print(answer)
while(True):
        equation=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
        #ncode the equation entered and the gets the decoded answer
        sock.sendto(equation.encode(), (serverName, serverport))
        answer = sock.recv(1024).decode('utf-8')
        #End the program
        if answer == "Q":
            quit();
            #Error called
        elif answer == "ZeroDiv":
            print("You can't divide by 0, try again")
        elif answer == "MathError":
            print("There is an error with your math, try again")
        elif answer == "SyntaxError":
            print("There is a syntax error, please try again")
        elif answer == "NameError":
            print("You did not enter an equation, try again")
            #Prints the answer if no errors
        else:
            print("The answer is:", answer)
  #close server and socket          
serverAddress.close()
sock.close()
