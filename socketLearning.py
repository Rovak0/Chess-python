import socket
import pygame
pygame.init()
from decoder import decoder


HOST = '' 
PORT = 5789
   
running = True

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
try:
    # With the help of bind() function 
    # binding host and port
    soc.bind((HOST, PORT))
      
except socket.error as message:
     
    # if any error occurs then with the 
    # help of sys.exit() exit from the program
   print("Failed to Bind")
"""     print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
    sys.exit() """
     
# print if Socket binding operation completed    
print('Socket binding operation completed')
  
# With the help of listening () function
# starts listening
soc.listen(10)
  
conn, address = soc.accept()
# print the address of connection
print('Connected with ' + address[0] + ':'
      + str(address[1]))

recMes = conn.recv(1024)
recMes = recMes.decode()
recMes = str(recMes)
print(recMes)

result = decoder(recMes)
print(result)
print(result.getContent())
# newNumb = message.encode()
# conn.send(recMes)

conn.close()