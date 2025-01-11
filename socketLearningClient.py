import socket
from chessBoard import board
import pygame
from chessPieces import pieceType

pygame.init()
font = pygame.font.SysFont('arial', 100)

HOST = "127.0.0.1"
PORT = 5789

recieving = True

mesPiece = pieceType(1, "paladin", "rook", 18, 4, (3,2), 12, 2)
mesSquare = board.square((0,0), 100, 100, 100, (150,150,150), font, mesPiece)
mesSquare = mesSquare.encode()
sendPiece = mesPiece.encode()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect((HOST, PORT))
message = mesSquare
data = None
soc.send(message)
data = soc.recv(1024)

print(data.decode())



