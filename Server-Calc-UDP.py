#References: https://docs.python.org/3/contents.html
#            https://github.com/aslattum/python-tcp-calculator
#            Core Python Application Programming 3rd Edition
#Created by Kevin Chau and Adriam Gonzlez

from math import * #Allows more math funcions to be entered
from socket import * #Import socket

serverName = 'localhost' #Get hostname
serverport = 12000 #Get server port
sock = socket(AF_INET, SOCK_DGRAM) #Create socket
sock.bind(('', serverport)) #bind socket to server port
print('The server is connected')
while True:
    try:
        equation, clientAddress = sock.recvfrom(1024)
        #Print the equation received in server side
        print ("Received: " + bytes(equation).decode())
        sEquation = bytes(equation).decode()
        #End the program
        if sEquation == "Q" or sEquation == "q" or sEquation == "Quit" or sEquation == "quit" or sEquation == "quit()":
            print ("Server Exiting")
            sock.sendto("Q".encode(), clientAddress)
            quit();
            break
        else:
            #Prints the equation again to confirm the equation is evaluated
            print("You gave me the equation:", sEquation)       
            answer = eval(equation)
            sock.sendto(str(answer).encode(), clientAddress)
   #Error called and calls client side   
    except (ZeroDivisionError):
        sock.sendto("ZeroDiv".encode(), clientAddress)
    except (ArithmeticError):
        sock.sendto("MathError".encode(), clientAddress)
    except (SyntaxError):
        sock.sendto("SyntaxError".encode(), clientAddress)
    except (NameError):
        sock.sendto("NameError".encode(), clientAddress)
        #close client and socket
clientAddress.close()
sock.close()
