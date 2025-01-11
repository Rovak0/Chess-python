#this file will interpret the inputs
from chessBoard import board
from chessPieces import pieceType


def decoder(string, start = 0):
    key = string [start : start+4] #take the 1st 4 characters (the identifier) after the start, which incldues "OPEN"
    result = None
    split_list = None
    if key == "squr":
        valueList = []
        split_list = [0,8,10,12]
        for i in split_list: 
            pass 



def decoder(string, start = 0):
    key = string [start : start+4] #take the 1st 4 characters (the identifier) after the start, which incldues "OPEN"
    result = None
    if key == "squr":
        valueList = []
        piece = None #make a piece placeholder
        valueList.append(string[start+8: start+10]) #grabs the values out of the list because their positions are known
        valueList.append(string[start+10: start+12])
        valueList.append(string[start+12: start+15])
        valueList.append(string[start+15: start+18])
        valueList.append(string[start+18: start+21])
        valueList.append(string[start+21: start+24])
        valueList.append(string[start+24: start+27])
        valueList.append(string[start+27: start+30])
        isPiece = (string[30])

        #recreate the square
        valueList[0] = float(valueList[0]) #a lot of values can't be strings
        valueList[1] = float(valueList[1])
        valueList[2] = float(valueList[2])
        valueList[3] = float(valueList[3])
        valueList[4] = float(valueList[4])
        valueList[5] = float(valueList[5])
        valueList[6] = float(valueList[6])
        valueList[7] = float(valueList[7])
        result = board.square((valueList[0], valueList[1]), valueList[2], valueList[3], valueList[4], (valueList[5],valueList[6],valueList[7]))
        if isPiece:
            piece = decoder(string, 31+start)
            result.setContent(piece)
    
    if key == "piec":
        length = string[start +4: start+8]
        valueList = []
        valueList.append(string[start+8: start+9]) #grabs the values out of the list because their positions are known
        valueList.append(string[start+9: start+13]) 
        valueList.append(float(string[start+13: start+15]))
        valueList.append(float(string[start+15: start+17])) 
        valueList.append(float(string[start+17: start+18]))
        valueList.append(float(string[start+18: start+19]))
        valueList.append(float(string[start+19: start+21]))
        valueList.append(float(string[start+21: start+23]))
        valueList.append(string[start+23: start+27]) 
        valueList.append(string[27]) 

        length = int(length)
        if length == 20:
            result = pieceType(valueList[0], valueList[1], [valueList[2], valueList[3]], valueList[4], valueList[5], valueList[6], valueList[7], valueList[8], shield= valueList[9])
        elif length == 29:
            valueList.append(float(string[start+28: start+30]))  #valueList[10]
            valueList.append(float(string[start+30: start+31]))
            valueList.append(float(string[start+31: start+33])) 
            valueList.append(float(string[start+33: start+35])) 
            valueList.append(float(string[start+35: start+37])) 
            result = pieceType(valueList[0], valueList[1], [valueList[2], valueList[3]], valueList[4], valueList[5], valueList[6], valueList[7], valueList[8], valueList[10], valueList[9], valueList[11], valueList[12],[valueList[13], valueList[14]])
    

    return result
