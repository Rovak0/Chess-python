import pygame
from chessPieces import pieceType
#from chessPieces import moveDict
import pieceData



class board:
    white = (255, 255, 255)
    color = (0,0,0)
    selectedColor = (200, 0, 0)

    #square things
    class square(pygame.sprite.Sprite): #
        def __init__(self, pos, x, y, squareSize, color, font = pygame.font.SysFont('arial', 100), content = None, squareSizeY = None): # 
            super().__init__()
            self.xPos = pos[0] #this is grid
            self.yPos = pos[1]
            self.x = x #this is pixel
            self.y = y
            self.squareSize = squareSize #how large are the squares?
            if squareSizeY:
                self.squareSizeY = squareSizeY
            else:
                self.squareSizeY = squareSize
            self.colorBase = color
            self.color = color #is it black or white?
            self.content = content #default contents of a square is empty
            if content:
                self.pieceStart()
            self.active = False
            self.backColor = None
            self.font = font
            self.center = ((x+(squareSize*0.5)), (y+(self.squareSizeY*0.5)))
            #self.rendering()
        
        def rendering(self):
            t_surf = self.font.render(None, True, self.color, None)
            self.image = pygame.Surface((self.squareSize, self.squareSize), pygame.SRCALPHA) 
            #self.image = pygame.Surface((max(self.squareSize+10, t_surf.get_width()), self.squareSize), pygame.SRCALPHA)  
            if self.backColor:
                self.image.fill(self.backColor)
            self.image.blit(t_surf, (5,5))
            pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
            self.rect = self.image.get_rect(topleft = (self.x, self.y))


        #Select box
        def updateBox(self, eventList):
            for event in eventList:
                if event.type == pygame.MOUSEBUTTONDOWN :#and self.rect.collidepoint(event.pos):
                    if self.rect.collidepoint(event.pos):
                        self.active = not self.active
                    #if self.active:
                        #self.color = (200, 0, 0) #change select color to be variable
                    #else:
                        #self.color = self.colorBase
                    #self.rendering()
                        
        def drawSprite(self, screen):
            spriteColor = pieceData.colorDict[self.getContent().getName()]
            pygame.draw.circle(screen, spriteColor, self.center, self.squareSize*.25)

        #what to do when a piece enters a tile
        def pieceEnter(self, newPiece):
            if self.content == None: #if the square is empty, just move the piece
                self.content == newPiece
            else: #if the square is occupied, take the piece before moving the 2nd piece
                self.content.captured()
                self.content == newPiece

        def pieceStart(self):
            self.content.setPos(self)
        
        #to send squares over sockets, they need to be encoded
        def encode(self):
            #need to send pos, x, y, squareSize, color, font
            finalMessage = ''
            mesLen = 0
            posStringX = str('%02d' % self.xPos) #2 int
            finalMessage = finalMessage + posStringX
            mesLen += len(posStringX)

            posStringY = str('%02d' % self.yPos) #2 int
            finalMessage = finalMessage + posStringY
            mesLen += len(posStringY)

            xString = str('%03d' % self.x) #3 int
            finalMessage = finalMessage + xString
            mesLen += len(xString)

            yString = str('%03d' % self.y) #3 int
            finalMessage = finalMessage + yString
            mesLen += len(yString)

            sizeString = str('%03d' % self.squareSize) # 3int
            mesLen += len(sizeString)
            finalMessage = finalMessage + sizeString

            #color is 3 numbers
            color1str = str('%03d' % self.color[0]) #3
            mesLen += len(color1str)
            finalMessage = finalMessage + color1str

            color2str = str('%03d' % self.color[1]) #3
            mesLen += len(color2str)
            finalMessage = finalMessage + color2str

            color3str = str('%03d' % self.color[2]) #3
            mesLen += len(color3str)
            finalMessage = finalMessage + color3str
        #figure out font later
            #need to encode piece in square
            if not self.getContent():
                pieceStr = "0"
                finalMessage = finalMessage + pieceStr
            else:
                pieceStr = "1"
                pieceInfo = self.getContent().getData() #1
                finalMessage = finalMessage + pieceStr
                finalMessage = finalMessage+ pieceInfo
            mesLen +=1
            ident = "squr"
            finalMessage = ident + str('%04d' % mesLen)+ finalMessage 
            #len should be 23

            finalMessage = finalMessage.encode()
            return finalMessage



        #getters and setters
        def getX(self):
            return self.x
        def getY(self):
            return self.y
        def getColor(self):
            return self.color
        def getContent(self):
            return self.content
        def getSize(self):
            return self.squareSize
        def getXpos(self):
            return self.xPos
        def getYpos(self):
            return self.yPos
        def getPosition(self):
            return (self.xPos, self.yPos)
        def getActive(self):
            return self.active
        def getBase(self):
            return self.colorBase
        
        def setActive(self, newActive):
            self.active = newActive
        def setX(self, newX):
            self.x = newX
        def setY(self, newY):
            self.y = newY
        def setContent(self, newContent):
            self.content = newContent
        def clearContent(self): #empty the square
            self.content = None
        def setColor(self, newColor):
            self.color = newColor
        def selectColor(self): #calls on the selecetedColor from board
            self.color = board.selectedColor







    #board things


    def __init__(self, size, font = pygame.font.SysFont('arial', 100) , topLeft = (0,0), boardSize = 8):
        self.boardSize = boardSize 
        self.size = size
        self.topLeft = topLeft
        self.font = font
    
    #create the board
    def generateBoard(self):
        squareList = [] #make a list to return for the main function.  End goal is a list of lists
        x = 0  #make variables to automate construction
        y = 0 
        whiteSquare = False #input variable for square color
        while x <self.boardSize: #count up until y is 7 (self.boardSize interations)
            xList = [] #make a y list
            while y < self.boardSize:
                if whiteSquare == True:
                    newSquare = self.square((x, y), 
                        x*self.size+ self.topLeft[0],
                        y*self.size + self.topLeft[1], 
                        self.size, 
                        self.white, 
                        self.font
                    )

                else:
                    newSquare = self.square((x, y), x*self.size+ self.topLeft[0], y*self.size + self.topLeft[1], self.size, self.color, font = self.font)
                y +=1
                xList.append(newSquare)
                whiteSquare = not whiteSquare #flip color each time
            y = 0 #reset the x for each y loop
            squareList.append(xList)
            if not (self.boardSize%2):
                whiteSquare = not whiteSquare #aself.boardSize color is the same as b1
            x += 1
        return squareList
    
    def makeOutline(self): #create outline for the board
        point1= self.topLeft
        point2 = (self.topLeft[0], self.topLeft[1] + self.boardSize*self.size)
        point3 = (self.topLeft[0]+ self.boardSize*self.size, self.topLeft[1] )
        point4 = (self.topLeft[0]+ self.boardSize*self.size, self.topLeft[1] + self.boardSize*self.size)
        return [point1, point2, point3, point4]
        

    
    def moveChecker(self, piece, boardState, currentLoc): #piece type, board, boardSizeX, boardSizeY, currentLoc
        moveType = pieceData.moveDict[piece.getMoveType()]
        notMoved = piece.getHasNotMoved()
        return moveType(boardState, self.boardSize, self.boardSize, currentLoc, piece.getSide(), notMoved, piece.getMoveCap())

    def movePiece(self, firstSqr, secondSqr, piece, legalMoves): 
        #piece = firstSqr.getContent()
        if (secondSqr.getXpos(), secondSqr.getYpos()) in legalMoves:
            piece.setHasNotMoved(0)
            piece.setPos(secondSqr)
            secondSqr.setContent(piece)
            firstSqr.setContent(None)

    #manage pawn upgrades
    def pawnUp(self, boardState):
        count = 0
        while count < self.boardSize:
            if boardState[count][0].getContent():
                if boardState[count][0].getContent().getName() == "pawn" and boardState[count][0].getContent().getSide() == 2:
                    boardState[count][0].setContent(pieceType("queen", 2))
            count +=1
        count = 0
        while count < self.boardSize:
            if boardState[count][self.boardSize-1].getContent():
                if boardState[count][self.boardSize-1].getContent().getName() == "pawn" and boardState[count][self.boardSize-1].getContent().getSide() == 1:
                    boardState[count][self.boardSize-1].setContent(pieceType("queen", 1))
            count +=1

