import pygame
import random
#moveDict["pawn"](boardState)


    #pieces
#class pieces:

class pieceType: #manage the different types of pieces

    d20 = random.randrange(1,21)

    def __init__(self, side, name, #swapped side and name to make dictionaries easier
                 location = None, hasNotMoved = 1, direction = 0, health = 1,  currentHealth = None, moveType = None, 
                 moveCap = None, shield = 0, ac = 0, attackMod = 0, damage = None): 
        #ac, moveType, attackMod, damage, health, absorb = 0, direction = "up"
        self.side = side
        self.name = name
        if location:
            self.location = location
        else:
            self.location = [-1, -1]
        if moveType:
            self.moveType = moveType
        else:
            self.moveType = name
        self.hasNotMoved = hasNotMoved
        self.ac = ac
        self.attackMod = attackMod #figure out how to have 2 damage types
        self.damage = damage
        self.direction = direction
        self.maxHealth = health
        if currentHealth:
            self.health = currentHealth
        else:
            self.health = health
        self.moveCap = moveCap
        self.shield = shield


    #attacking
    def attack(self, target, modifiers): #modifiers will have to be a list
        #find attack total
        theRoll = self.d20
        totalMod = 0
        for item in modifiers:
            totalMod += item
        toHit = theRoll+self.attackMod +totalMod #modifiers will have to be subscripted
        if theRoll >=19:
            return "crit"
        elif toHit >= target.getAC(): #compare to target's ac
            return "hit"
        else:
            return "miss"

    #damage on hit
    def dealDamage(self, modifiers): #modifiers will be a list
        damageRoll = random.randrange(1,self.damage+1) #rand range does not include end point
        return damageRoll + modifiers
    
    #changing health
    def healthChange(self, change):
        self.health += change

    #recieving damage
    def recieveDamage(self, damage):
        totalDamage = damage-self.absorb
        self.healthChange(-totalDamage)


    def drawSprite(self, screen, xScreen, yScreen, size):
        pygame.draw.circle(screen, (0,255,0), xScreen, yScreen, size)


    def getData(self): #this exists to get data for square encoding
        sideStr = str(self.side) #1 char
        nameStr = str(self.name) #4 char
        #location is a list
        posXStr = str('%02d' % self.location[0]) #2 char
        posYStr = str('%02d' % self.location[1]) #2 char
        movedStr = str(self.hasNotMoved) #bool
        directionStr = str(self.direction) #int
        healthStr = str('%02d' % self.health) #2 int
        maxHealthStr = str('%02d' % self.maxHealth) #2 digit int
        moveTypeStr = str(self.moveType) #4 char
        shieldStr = str(self.shield)

        finalString = sideStr +nameStr + posXStr +posYStr +movedStr +directionStr +healthStr +maxHealthStr +moveTypeStr +shieldStr

    #these variables may or may not exist
        if self.moveCap: #1 int
            moveCapStr = str(self.moveCap)
            finalString = finalString+moveCapStr
        if self.ac: #2 int
            acStr = str(self.ac)
            finalString = finalString+acStr
    #there may be 2 attacks
        if self.attackMod: #2 int or list
            if type(self.attackMod) == list:
                attackStr = str('%02d' % self.attackMod[0]) + str('%02d' % self.attackMod[1])
            else:
                attackStr = str('%02d' % self.attackMod)
            finalString = finalString+attackStr
            #tuple can be sent, so an attack list should be fine
        if self.damage: #list of 2
            if type(self.damage[0]) == list: #4 or 8
                damStr = str('%02d' % self.damage[0])+str('%02d' % self.damage[1])+str('%02d' % self.damage[2])+str('%02d' % self.damage[3])
            else:
                damStr = str('%02d' %self.damage[0]) + str('%02d' % self.damage[1])
            finalString = finalString+damStr

        #identifier - info - closer
        start = "piec"
        mesLen = str('%04d' % len(finalString))
        finalString = start + mesLen + finalString
        return finalString #output the bytes
    




    def encode(self): #this is to send specifically a piece
        sideStr = str(self.side) #1 char
        nameStr = str(self.name) #4 char
        #location is a list
        posXStr = str('%02d' % self.location[0]) #2 char
        posYStr = str('%02d' % self.location[1]) #2 char
        movedStr = str(self.hasNotMoved) #bool
        directionStr = str(self.direction) #int
        healthStr = str('%02d' % self.health) #2 int
        maxHealthStr = str('%02d' % self.maxHealth) #2 digit int
        moveTypeStr = str(self.moveType) #4 char
        shieldStr = str(self.shield)

        finalString = sideStr +nameStr + posXStr +posYStr +movedStr +directionStr +healthStr +maxHealthStr +moveTypeStr+shieldStr

    #these variables may or may not exist
        if self.moveCap: #1 int
            moveCapStr = str(self.moveCap)
            finalString = finalString+moveCapStr
        if self.ac: #2 int
            acStr = str(self.ac)
            finalString = finalString+acStr
    #there may be 2 attacks
        if self.attackMod: #2 int or list
            if type(self.attackMod) == list:
                attackStr = str('%02d' % self.attackMod[0]) + str('%02d' % self.attackMod[1])
            else:
                attackStr = str('%02d' % self.attackMod)
            finalString = finalString+attackStr
            #tuple can be sent, so an attack list should be fine
        if self.damage: #list of 2
            if type(self.damage[0]) == list:
                damStr = str('%02d' % self.damage[0])+str('%02d' % self.damage[1])+str('%02d' % self.damage[2])+str('%02d' % self.damage[3])
            else:
                damStr = str(self.damage[0]) + str('%02d' % self.damage[1])
            finalString = finalString+damStr

        #identifier - info - closer
        start = "piec"
        mesLen = str('%04d' % len(finalString))
        finalString = start + mesLen + finalString
        finalString = finalString.encode() #turn the long string into bytes
        return finalString #output the bytes





    def getAC(self):
        return self.ac
    def getAttackMod(self):
        return self.attackMod
    def getDamage(self):
        return self.damage
    def getDirection(self):
        return self.direction
    def getHasNotMoved(self):
        return self.hasNotMoved
    def getHealth(self):
        return self.health
    def getMaxHealth(self):
        return self.maxHealth
    def getMoveCap(self):
        return self.moveCap
    def getMoveType(self):
        return self.moveType
    def getName(self):
        return self.name
    def getShield(self):
        return self.shield
    def getSide(self):
        return self.side
    def getPos(self):
        return self.location
    def getX(self):
        return self.location[0]
    def getY(self):
        return self.location[1]
    

    def setHasNotMoved(self, bool):
        self.hasNotMoved = bool
    def setHealth(self, newHealth):
        self.health = newHealth
    def setDirection(self, newDirection):
        self.direction = newDirection
    def setPos(self, newPos): #pos is a list, so changing the components sets the new pos
        newPos = newPos.getPosition()
        self.setX(newPos[0])
        self.setY(newPos[1])
    def setX(self, newX):
        self.location[0] = newX
    def setY(self, newY):
        self.location[1] = newY


