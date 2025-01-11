import pygame
pygame.init()
from chessBoard import board
from chessPieces import pieceType as pieces
import pieceData

#font = pygame.font.SysFont('arial', 100)
# Initializing surface

surface = pygame.display.set_mode((1000,750))
# Initializing Color
color = (255,0,0)
selectColor1 = (0,0,255)
selectColor2 = (255, 0,0)
selColors = [selectColor1, selectColor2]
 
#create board
theBoard = board(75)#, font
squareList = theBoard.generateBoard()
outline = theBoard.makeOutline()

#create the sprites for the board squares
boardGroup = []
for object in squareList: #run through each y list in squareList
    for item in object: #run through each x in y list
        item.rendering() #turn on rendering
        boardGroup.append(item)
#boardSprites = pygame.sprite.Group(boardGroup) 



count1 = 0
count1pawn = 0
count2 = 0
count2pawn = 0
for item in pieceData.placeDict["base"]:
    if item[1] == 1:
        if item[0] != "pawn":
            squareList[count1][0].setContent(pieces(1, item[0], location = [count1,0]))
            count1 +=1
        else:
            squareList[count1pawn][1].setContent(pieces(1, item[0], location = [count1pawn,0]))
            count1pawn +=1
    elif item[1] == 2:
        if item[0] != "pawn":
            squareList[count2][7].setContent(pieces(2, item[0], location = [count2,0]))
            count2 +=1
        else:
            squareList[count2pawn][6].setContent(pieces(2, item[0], location = [count2pawn,0]))
            count2pawn +=1

# squareList[0][0].setContent(pieces("queen", 1, moveCap = 4))
# squareList[4][4].setContent(pieceData.fantasyPieces["monk1"])
# squareList[4][4].getContent().setX(4)
# squareList[4][4].getContent().setY(4)

running = True
selectedTiles = []
lastMoveAction = None

#create a list of pieces on the board for future use
pieceList = []
for tileList in squareList:
    for tile in tileList:
        if tile.getContent():
            pieceList.append(tile.getContent())


index = 0

while running:

    #managing inputs
    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        for tile in boardGroup:
            tile.updateBox(event_list)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tile.rect.collidepoint(event.pos): #check if tile is active
                    if len(selectedTiles)==0: #is 0 tiles selected
                        selectedTiles.append(tile)
                    elif len(selectedTiles)==1: #is 1 tile selected
                        if tile.getActive():
                            selectedTiles.insert(0, tile)
                        else:
                            selectedTiles.pop()
                    else: #are 2 tiles selected
                        selectedTiles[1] = selectedTiles[0]
                        selectedTiles[0] = tile



    #moving pieces
    if len(selectedTiles) == 2:
        if selectedTiles[1].getContent():
            legalMovesBoth = theBoard.moveChecker(selectedTiles[1].getContent(), squareList, (selectedTiles[1].getXpos(), selectedTiles[1].getYpos()))
            if selectedTiles[1].getContent().getAC(): #only fantasy pieces have ac
                legalMove = legalMovesBoth[1]
            else:
                legalMove = legalMovesBoth[0]
            
            theBoard.movePiece(selectedTiles[1], selectedTiles[0], selectedTiles[1].getContent(), legalMove)
            selectedTiles = [] #make the selected tiles an empty list
            # selectedTiles.pop() #clear list contents
            # selectedTiles.pop()
            for tile in boardGroup: #reset the active state of the entire board
                tile.setActive(tile.setActive(False))

#checking squares for updates
    theBoard.pawnUp(squareList)
    #check for dead pieces
    for piece in pieceList:
        if piece.getHealth() <= 0: # health is 0 or less
            pos = piece.getPos()
            squareList[pos[0]][pos[1]].setContent(None)



# Drawing the board
    for tile in boardGroup:
        pygame.draw.rect(surface, tile.getColor(), pygame.Rect(tile.getX(), tile.getY(), tile.getSize(), tile.getSize())) 
    #boardSprites.draw(surface)
        
    #coloring squares
    selColorIndex = 0 #used to track which color selected tiles are
    for tile in boardGroup: #reset the tile colors
        tile.setColor(tile.getBase())
    for tile in selectedTiles: #selected tile colors
        tile.setColor(selColors[selColorIndex])
        selColorIndex+=1
    for tile in selectedTiles: #coloring legal moves
        if tile.getContent():
            legalMove = theBoard.moveChecker(selectedTiles[0].getContent(), squareList, (selectedTiles[0].getXpos(), selectedTiles[0].getYpos())) #get legal moves
            if selectedTiles[0].getContent().getAC(): #only fantasy pieces have ac
                legalMove = legalMove[1] #get which set of moves
            else:
                legalMove = legalMove[0]

            for move in legalMove:
                squareList[move[0]][move[1]].setColor((0,255,0)) #color tiles

   
        
    #draw the contents of each square last
    for tile in boardGroup:
        if tile.getContent():
            tile.drawSprite(surface)

    pygame.draw.line(surface, (0,0, 255), outline[0], outline[1])
    pygame.draw.line(surface, (0,0, 255), outline[0], outline[2])
    pygame.draw.line(surface, (0,0, 255), outline[1], outline[3])
    pygame.draw.line(surface, (0,0, 255), outline[2], outline[3])

    #pygame.draw.rect(surface, color, pygame.Rect(100, 30, 100, 60))
    pygame.display.flip()

pygame.quit()
exit()
