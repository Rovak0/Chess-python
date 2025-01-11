from chessPieces import pieceType

#pawn functions
def pawnMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap): #Board is a list of lists.  current loc is in (x, y).  Side is 1 or 2
    x = currentLoc[0]
    y = currentLoc[1]
    emptyMoves = [] 
    allMoves = []

    #foward move
    if side == 1: #pawns move up or down the board depending on which side they are on
        if ((y + 1) < boardSizeY): #check if piece is at back of board
            if board[x][y+1].getContent() == None: #check if spot is empty
                emptyMoves.append((x,y+1))
                allMoves.append((x,y+1))

        #take
        if (x != 0) and (y < boardSizeY-1): #check if at left or back
            if (board[x-1][y+1].getContent() != None) : #check if spot is occupied
                if (board[x-1][y+1].getContent().getSide() != side):
                    allMoves.append((x-1, y+1))

        if (x+1 < boardSizeX) and (y < boardSizeY-1): #check if at right or back
            if board[x+1][y+1].getContent() != None: #check if spot is occupied
                if (board[x+1][y+1].getContent().getSide() != side):
                    allMoves.append((x+1, y+1))
        
        #en pessant
        if hasNotMoved:
            if board[x][y+1].getContent() == None and board[x][y+2].getContent() == None:
                emptyMoves.append((x, y+2))
                allMoves.append((x, y+2))

    
    if side == 2: #pawns move up or down the board depending on which side they are on
        if ((y - 1) >= 0): #check if piece is at back of board
            if board[x][y-1].getContent() == None: #check if spot is empty  Need to check piece side (can't take friendlies)
                allMoves.append((x,y-1))
                emptyMoves.append((x, y-1))
        #take
        if (x != 0) and ((y - 1) >= 0): #check if at left or back
            if board[x-1][y-1].getContent() != None: #check if spot is occupied
                if (board[x-1][y-1].getContent().getSide() != side):
                    allMoves.append((x-1, y-1))

        if (x+1 < boardSizeX) and ((y-1) >= 0): #check if at right or back
            if board[x+1][y-1].getContent() != None: #check if spot is occupied
                if (board[x+1][y-1].getContent().getSide() != side):
                    allMoves.append((x+1, y-1))
    
        #en pessant
        if hasNotMoved:
            if board[x][y-1].getContent() == None and board[x][y-2].getContent() == None:
                emptyMoves.append((x, y-2))
                allMoves.append((x, y-2))

    
    legalMoves = [allMoves, emptyMoves]
    return legalMoves

#king functions
def kingMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap):
    x = currentLoc[0]
    y = currentLoc[1]
    boardSizeX -=1
    boardSizeY -=1
    allMoves = []
    emptyMoves = []
    

#make a 3x3 square centered on king and check all tiles

    if x-1>=0: # find out if the x side leaves the board
        lowX = x-1
    else:
        lowX = 0
    if x+1<=boardSizeX:
        highX = x+1
    else: 
        highX = boardSizeX
    
    if y-1>=0:# find out if the y side leaves the board
        lowY = y-1
        resetY = y-1
    else:
        lowY = 0
        resetY = 0
    if y+1<=boardSizeY:
        highY = y+1
    else: 
        highY = boardSizeY

    xTracer = lowX
    yTracer = lowY
    while xTracer <= highX: #run a loop for x
        while yTracer <= highY: #run a loop for y 2nd to get x,y
            if board[xTracer][yTracer].getContent(): #check if there are contents
                if board[xTracer][yTracer].getContent().getSide() != side: #check if it is a friendly
                    allMoves.append((xTracer, yTracer))
            else: #empty square
                allMoves.append((xTracer, yTracer))
                emptyMoves.append((xTracer, yTracer))
            yTracer +=1 #breaks out of y loop
        yTracer = resetY #reset the y
        xTracer +=1 #break out of x loop
    legalMoves = (allMoves, emptyMoves)
    return legalMoves   

#rook functions
def rookMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap):
    x = currentLoc[0] 
    y = currentLoc[1]
    runXdown = False
    runXup = False
    runYdown = False
    runYup = False

    allMove = []
    emptyMove = []

    if moveCap: #check if there is a move limit
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1
    if x > 0: #check if left edge
        runXdown = True #if not, add left to move list

    while runXdown and tracer: 
        if x <= 0: #hit left wall, stop
            runXdown = False
            break
        if not board[x-1][y].getContent():#add one left
            allMove.append((x-1, y))
            emptyMove.append((x-1, y))
        if board[x-1][y].getContent(): #hit item stop
            if board[x-1][y].getContent().getSide() != side:
                allMove.append((x-1, y)) #add the new entry to the list before leaving the loop
            runXdown = False
        x -=1
        if moveCap: #if there is a cap, lower tracer
            tracer -=1
        
    x = currentLoc[0] #reset the x
    #print(x)
    if moveCap: #reset tracer
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1
    
    if x < boardSizeX: #check to see if it can move right
        runXup = True
    while runXup and tracer:
        if x >= (boardSizeX-1): #check if the new spot is at the edge
            runXup = False #end if it is
            break
        if not board[x+1][y].getContent():
            allMove.append((x+1, y))#add the new move to the list
            emptyMove.append((x+1, y))
        if board[x+1][y].getContent(): #check for colision
            if board[x+1][y].getContent().getSide() != side:
                allMove.append((x+1, y))
            runXup = False #stop on colision
        x +=1 #increase the x tracker
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    if moveCap: #reset tracer
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1
    x = currentLoc[0]
    #repeat for y
    if y > 0: #check if left edge
        runYdown = True #if not, add left to move list

    while runYdown and tracer: 
        if y <= 0: #hit left wall, stop
            runYdown = False
            break
        if not board[x][y-1].getContent():
            allMove.append((x, y-1))
            emptyMove.append((x, y-1))
        if board[x][y-1].getContent(): #hit item stop
            if board[x][y-1].getContent().getSide() != side:
                allMove.append((x, y-1))
            runYdown = False
        y -=1
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    if moveCap: #reset tracer
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1
    y = currentLoc[1] #reset the y
    #print(y + 100)
    if y < boardSizeY:
        runYup = True

    while runYup and tracer:
        if y >= (boardSizeY-1):
            runYup = False
            break
        if not board[x][y+1].getContent():
            allMove.append((x, y+1))
            emptyMove.append((x, y+1))
        if board[x][y+1].getContent():
            if board[x][y+1].getContent().getSide() != side:
                allMove.append((x, y+1))
            runYup = False
        y +=1
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    legalMoves = [allMove, emptyMove]
    return legalMoves

#bishop
def bisMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap):
    emptyMoves = []
    allMoves = []
    x = currentLoc[0] 
    y = currentLoc[1]
    if moveCap: #check if there is a move limit
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1

    while (x >0) and (y>0) and tracer:
        y-=1 #move the piece
        x-=1
        if board[x][y].getContent(): #check for collision, then break if hit
            if board[x][y].getContent().getSide()!=side:
                allMoves.append((x,y))
                emptyMoves.append((x,y))
            break
        allMoves.append((x,y)) #add the move to list

        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    x = currentLoc[0] 
    y = currentLoc[1]
    if moveCap: #check if there is a move limit
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1

    while (x >0) and (y<(boardSizeY-1)) and tracer:   
        y+=1 #move the piece
        x-=1
        if board[x][y].getContent(): #check for collision, then break if hit
            if board[x][y].getContent().getSide()!=side:
                allMoves.append((x,y))
                emptyMoves.append((x,y))
            break
        allMoves.append((x,y)) #add the move to list
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    x = currentLoc[0] 
    y = currentLoc[1]
    if moveCap: #check if there is a move limit
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1
    
    while (x <(boardSizeX-1))and (y>0) and tracer:
        y-=1 #move the piece
        x+=1
        if board[x][y].getContent(): #check for collision, then break if hit
            if board[x][y].getContent().getSide()!=side:
                allMoves.append((x,y))
                emptyMoves.append((x,y))
            break
        allMoves.append((x,y)) #add the move to list
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    x = currentLoc[0] 
    y = currentLoc[1]
    if moveCap: #check if there is a move limit
        tracer = moveCap
    else: #if not set the tracer to any number
        tracer = 1

    while (x <(boardSizeX-1))and (y<(boardSizeY-1)) and tracer:
        y+=1 #move the piece
        x+=1
        if board[x][y].getContent(): #check for collision, then break if hit
            if board[x][y].getContent().getSide()!=side:
                allMoves.append((x,y))
                emptyMoves.append((x,y))
            break
        allMoves.append((x,y)) #add the move to list
        if moveCap: #if there is a cap, lower tracer
            tracer -=1

    legalMoves = [allMoves, emptyMoves]
    return legalMoves

#queen
def queenMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap):
    legalMoves = []
    rookSide = rookMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap)
    bisSide = bisMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap)
    allMove = rookSide[0] + bisSide[0]
    emptyMove = rookSide[1] + bisSide[1]
    legalMoves = [allMove, emptyMove]
    return legalMoves

#knight
def knightMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap):
    emptyMoves = []
    allMoves = []
    x = currentLoc[0]
    y = currentLoc[1]
    if (x-2) >=0: #left 
        if (y+1) <boardSizeY: #and down #fix this later
            if board[x-2][y+1].getContent():
                if board[x-2][y+1].getContent().getSide()!=side:
                    allMoves.append((x-2, y+1))
            else:
                allMoves.append((x-2, y+1))
                emptyMoves.append((x-2, y+1))
        if (y-1) >= 0: #and up
            if board[x-2][y-1].getContent():
                if board[x-2][y-1].getContent().getSide()!=side:
                    allMoves.append((x-2, y-1))
            else:
                allMoves.append((x-2, y-1))
                emptyMoves.append((x-2, y-1))
    if (x+2) <boardSizeX: #right
        if (y+1) <boardSizeY:
            if board[x+2][y+1].getContent():
                if board[x+2][y+1].getContent().getSide()!=side:
                    allMoves.append((x+2, y+1))
            else:
                allMoves.append((x+2, y+1))
                emptyMoves.append((x+2, y+1))
        if (y-1) >= 0:
            if board[x+2][y-1].getContent():
                if board[x+2][y-1].getContent().getSide()!=side:
                    allMoves.append((x+2, y-1))
            else:
                allMoves.append((x+2, y-1))
                emptyMoves.append((x+2, y-1))
    if (x-1) >=0:
        if (y+2) <boardSizeY:
            if board[x-1][y+2].getContent():  
                if board[x-1][y+2].getContent().getSide()!=side:  
                    allMoves.append((x-1, y+2))
            else:
                allMoves.append((x-1, y+2))
                emptyMoves.append((x-1, y+2))
        if (y-2) >= 0:
            if board[x-1][y-2].getContent():
                if board[x-1][y-2].getContent().getSide()!=side:
                    allMoves.append((x-1, y-2))
            else:
                allMoves.append((x-1, y-2))
                emptyMoves.append((x-1, y-2))
    if (x+1) <boardSizeX:
        if (y+2) <boardSizeY:
            if board[x+1][y+2].getContent():
                if board[x+1][y+2].getContent().getSide()!=side:
                    allMoves.append((x+1, y+2))
            else:
                allMoves.append((x+1, y+2))
                emptyMoves.append((x+1, y+2))
        if (y-2) >= 0:
            if board[x+1][y-2].getContent():
                if board[x+1][y-2].getContent().getSide()!=side:
                    allMoves.append((x+1, y-2))
            else:
                allMoves.append((x+1, y-2))
                emptyMoves.append((x+1, y-2))
    legalMoves = [allMoves, emptyMoves]
    return legalMoves

def monkMove(board, boardSizeX, boardSizeY, currentLoc, side, hasNotMoved, moveCap): #monk moves three in any direction (not straight line)
    x = currentLoc[0]
    y = currentLoc[1]
    allMove = []
    emptyMove = []

    tracer = 0
    kingList = kingMove(board, boardSizeX, boardSizeY, (x,y), side, hasNotMoved, moveCap)
    checkList = [kingList[1]]
    allMoveHolder = []
    emptyMoveHolder = kingList[1]
    allMoveHolder = allMoveHolder + kingList[0]
    tracer +=1
    while tracer < moveCap:
        holdingList = [] #an empty list to hold lists to check
        for item in checkList[tracer-1]: #looks at each square in the empty move of the current king loop
            #for object in item:
            kingList = kingMove(board, boardSizeX, boardSizeY, item, side, hasNotMoved, moveCap) #item is x,y
            #holdingList = holdingList + kingList[1] #add the next list to check to the holding list
            for item in kingList[1]: #brings the list of tile into tiles
                if item not in holdingList:
                    holdingList.append(item) #adds tiles
            for item in kingList[0]:
                if item not in allMoveHolder:
                    allMoveHolder.append(item)
            #allMoveHolder = allMoveHolder +kingList[0]
        checkList.append(holdingList) #add the holding list to the check list
        for item in holdingList:
            if item not in emptyMoveHolder:
                emptyMoveHolder.append(item)
        tracer +=1 #increase tracer
    
    for item in emptyMoveHolder: #the items are lists
        if item not in emptyMove:
            emptyMove.append(item)
    for item in allMoveHolder: #the items are lists
        if item not in allMove:
            allMove.append(item)
    #print(emptyMove)
    legalMoves = [allMove, emptyMove]
    return legalMoves



moveDict = {
    "pawn" : pawnMove, #basic move.  Add taking piece later 
    "rook" : rookMove,
    "king" : kingMove,
    "bish" : bisMove,
    "quee" : queenMove,
    "knig" : knightMove,
    "monk" : monkMove
}


#piece sprites
colorDict = {
    "pawn" : (255, 0, 255), #basic move.  Add taking piece later 
    "rook" : (255,255,0),
    "king" : (150,150,0),
    "bish" :(0, 150, 150),
    "quee" : (150, 0, 150),
    "knig" : (0, 255, 255),
    "monk" : (150, 150, 150)
}

placeDict = {
    "base" : [["rook", 1],["knig", 1],["bish",1], ["quee", 1], ["king", 1],["bish",1], ["knig", 1],["rook", 1],
              ["pawn", 1],["pawn", 1],["pawn", 1],["pawn", 1],["pawn", 1],["pawn", 1],["pawn", 1],["pawn", 1],
              ["rook", 2],["knig", 2],["bish",2], ["quee", 2], ["king", 2],["bish",2], ["knig", 2],["rook", 2],
              ["pawn", 2],["pawn", 2],["pawn", 2],["pawn", 2],["pawn", 2],["pawn", 2],["pawn", 2],["pawn", 2]]
}

#side, name, moveType, ac = 0, attackMod = 0, damage = (0,0), health = 1, moveCap = None, shield = False, direction = "up"
#self, side, name, #swapped side and name to make dictionaries easier
                # moveType = None, location = None, hasNotMoved = True, direction = "up", health = 1,  currentHealth = None,
                 #moveCap = None, shield = False, ac = 0, attackMod = 0, damage = None
fantasyPieces = {
    "paladin1" : pieceType(1, "pala", moveType="rook", ac = 18, attackMod=4, damage = [3,2], health=12, moveCap= 2),
    "paladin2" : pieceType(2, "pala", moveType="rook", ac = 18, attackMod=4, damage = [3,2], health=12, moveCap= 2),
    "queen1" : pieceType(1, "quee", moveType="king", ac = 11, attackMod=3, damage = [2,2], health=12, moveCap= 1),
    "queen2" : pieceType(2, "quee", moveType="king", ac = 11, attackMod=3, damage = [2,2], health=12, moveCap= 1),
    "king1" : pieceType(1, "king", moveType="king", ac = 16, attackMod=5, damage=[3,2], health=12, moveCap= 1),
    "king2" : pieceType(2, "king", moveType="king", ac = 16, attackMod=5, damage=[3,2], health=12, moveCap= 1),
    "knight1" : pieceType(1, "knig", moveType="knig", ac = 16, attackMod=8, damage = [2,3], health=12, moveCap= None),
    "knight2" : pieceType(2, "knig", moveType="knig", ac = 16, attackMod=8, damage = [2,3], health=12, moveCap= None),
    "crusader1" : pieceType(1, "crus", moveType="bish", ac = 20, attackMod=6, damage = [6,1], health=12, moveCap= 2, shield = True),
    "crusader2" : pieceType(2, "crus", moveType="bish", ac = 20, attackMod=6, damage = [6,1], health=12, moveCap= 2, shield = True),
    "ranger1" : pieceType(1, "rang", moveType="bish", ac = 14, attackMod=[6,3], damage = [[2,2], [1,4]], health=10, moveCap= 2),
    "ranger2" : pieceType(2, "rang", moveType="bish", ac = 14, attackMod=[6,3], damage = [[2,2], [1,4]], health=10, moveCap= 2),
    "warrior1" : pieceType(1, "warr", moveType="quee", ac = 14, attackMod=6, damage = [4,2], health=16, moveCap= 2),
    "warrior2" : pieceType(2, "warr", moveType="quee", ac = 14, attackMod=6, damage = [4,2], health=16, moveCap= 2),
    "monk1" : pieceType(1, "monk", moveType="monk", ac = 15, attackMod=8, damage = [1,6], health=10, moveCap= 3),
    "monk2" : pieceType(2, "monk", moveType="monk", ac = 15, attackMod=8, damage = [1,6], health=10, moveCap= 3),
    "musketeer1" : pieceType(1, "musk", moveType="bish", ac = 15, attackMod=[6,4], damage = [[2,3], [1,5]], health=10, moveCap= 2),
    "musketeer2" : pieceType(2, "musk", moveType="bish", ac = 15, attackMod=[6,4], damage = [[2,3], [1,5]], health=10, moveCap= 2),
    "assassin1" : pieceType(1, "assa", moveType="quee", ac = 16, attackMod=10, damage = [3,2], health=10, moveCap= 2),
    "assassin2" : pieceType(2, "assa", moveType="quee", ac = 16, attackMod=10, damage = [3,2], health=10, moveCap= 2),
    "wizard1" : pieceType(1, "wiza", moveType="king", ac = 10, attackMod=1, damage = [1,4], health=8, moveCap= 1),
    "wizard2" : pieceType(2, "wiza", moveType="king", ac = 10, attackMod=1, damage = [1,4], health=8, moveCap= 1),
    "cleric1" : pieceType(1, "cler", moveType="king", ac = 10, attackMod=1, damage = [2,2], health=8, moveCap= 1),
    "cleric2" : pieceType(2, "cler", moveType="king", ac = 10, attackMod=1, damage = [2,2], health=8, moveCap= 1),
}