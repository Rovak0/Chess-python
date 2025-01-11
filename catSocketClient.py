import socket
import pygame
pygame.init()
from chessBoard import board
from chessPieces import pieceType
import pieceData

pygame.init()
font = pygame.font.SysFont('arial', 100)

HOST = "127.0.0.1"
PORT = 5789

recieving = True
piece = pieceData.fantasyPieces["monk1"]

mesPiece = pieceType(1, "rook") #, "monk", 18, 4, (3,2), 12, 2
mesSquare = board.square((0,0), 100, 100, 100, (150,150,150), content =piece) #, font
mesSquare = mesSquare.encode()
sendPiece = mesPiece.encode()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect((HOST, PORT))
message = mesSquare
data = None
soc.send(message)
data = soc.recv(1024)

print(data.decode())