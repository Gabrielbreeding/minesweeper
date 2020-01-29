#!/usr/bin/python3
#GabrielBreeding

'''a program where the user can interact with a list to reveal the lists true contents'''


#---------------imports------------------
import sys
import random as r

def makefield(field):
    if field == 1:
        return [['#' , '#' , '#', '#', '#'],
                 ['#' , '#' , '#', '#', '#'],
                 ['#' , '#' , '#', '#', '#'],
                 ['#' , '#' , '#', '#', '#'],
                 ['#' , '#' , '#', '#', '#']]
    elif field == 2:
        return [['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-']]

field = makefield(1)
revealed = makefield(2)

def placebomb():
    #places the bombs
    bombs = 0
    while bombs < 4:
        x = r.randint(0, 4)
        y = r.randint(0, 4)
        while revealed[y][x] == 'M':
            x = r.randint(0,4)
            y = r.randint(0,4)
        revealed[y][x] = 'M'
        bombs += 1
placebomb()

def getnum(number):
    '''
    This function will find the specified number on the screen and add them to a dictionary.
    
    for loop and nested for loop to look through every point.
    when selected point is the specified number it will add it to the dictionary with 2 definitions, row and column.
    '''
    
    numbers = {}
    num = 0
    for row in range(newlist):
        for column in range(newlist[row]):
            if newlist[row][column] == number:
                num += 1
                numbers[str(num)] = (row, column)
    
    return numbers 
def placenums():
    c = 0
    cc = 0
    for box in (revealed):
        cc = 0
        if c > 4:
            c = 0
        for boxes in revealed[c]:
            if cc > 4:
                cc = 0
            if revealed[c][cc] == 'M':
                c = c
                cc = cc
            else:
                if c == 0:
                    if cc == 1:
                        middle = revealed[c][:3].count('M')
                        bottom = revealed[c+1][:3].count('M')
                        tM = (middle + bottom) 
                    elif cc == 0:
                        middle = revealed[c][:2].count('M')
                        bottom = revealed[c+1][:2].count('M')
                        tM = (middle + bottom)  
                    elif cc == 4:
                        middle = revealed[c][3:].count('M')
                        bottom = revealed[c+1][3:].count('M')
                        tM = (middle + bottom)
                    elif cc == 2:
                        middle = revealed[c][1:4].count('M')
                        bottom = revealed[c+1][1:4].count('M')
                        tM = (middle + bottom)
                    elif cc == 3:
                        middle = revealed[c][2:].count('M')
                        bottom = revealed[c+1][2:].count('M')
                        tM = (middle + bottom)
                elif c == 4:
                    if cc == 1:
                        top = revealed[c-1][:3].count('M')
                        middle = revealed[c][:3].count('M')
                        tM = (top + middle)
                    elif cc == 0:
                        top = revealed[c-1][:2].count('M')
                        middle = revealed[c][:2].count('M')
                        tM = (top + middle)                
                    elif cc == 4:
                        top = revealed[c-1][3:].count('M')
                        middle = revealed[c][3:].count('M')
                        tM = (top + middle) 
                    elif cc == 3:
                        top = revealed[c-1][2:].count('M')
                        middle = revealed[c][2:].count('M')
                        tM = (top + middle)
                    elif cc == 2:
                        top = revealed[c-1][1:4].count('M')
                        middle = revealed[c][1:4].count('M')
                        tM = (top + middle)
                elif c > 0 and c < 4:
                    if cc == 1:
                        top = revealed[c-1][:3].count('M')
                        middle = revealed[c][:3].count('M')
                        bottom = revealed[c+1][:3].count('M')
                        tM = (top + middle + bottom)
                    elif cc == 0:
                        top = revealed[c-1][:2].count('M')
                        middle = revealed[c][:2].count('M')
                        bottom = revealed[c+1][:2].count('M')
                        tM = (top + middle + bottom)
                    elif cc == 4:
                        top = revealed[c-1][3:].count('M')
                        middle = revealed[c][3:].count('M')
                        bottom = revealed[c+1][3:].count('M')
                        tM = (top + middle + bottom)
                    elif cc == 2:
                        top = revealed[c-1][1:4].count('M')
                        middle = revealed[c][1:4].count('M')
                        bottom = revealed[c+1][1:4].count('M')
                        tM = (top + middle + bottom)
                    elif cc == 3:
                        top = revealed[c-1][2:].count('M')
                        middle = revealed[c][2:].count('M')
                        bottom = revealed[c+1][2:].count('M')
                        tM = (top + middle + bottom)            
                revealed[c][cc] = tM    
            cc += 1
        c += 1
placenums()

def getrow(version):
    if version == "R":
        place_flag = False
        print("        ")
        print("        ")
        print("Enter 'exit' to leave program")
        print("Or Enter 'flag' to place a flag")
        revrow = input("Please select which row to reveal: ")
        if revrow == "exit":
            print("Goodbye!")
            sys.exit()
        elif revrow == "flag" or revrow == "Flag":
            return "F"
        elif revrow not in selrow:
            print("        ")
            print("        ")
            print("ERROR:  Please enter a valid number.")
            hold()
            return getrow("R")
        return revrow
    if version == "F":
        place_flag = True
        print("        ")
        print("        ")
        print("Enter 'exit' to leave program")
        print("Or Enter 'back' to go back")
        revrow = input("Please select which row to flag: ")
        if revrow == "exit":
            print("Goodbye!")
            sys.exit()
        elif revrow == "back" or revrow == "Back":
            return getrow("R")
        elif revrow not in selrow:
            print("        ")
            print("        ")
            print("ERROR:  Please enter a valid number.")
            hold()
            return getrow("F")
        return revrow

def getcollumn(version):
    if version == "R":
        place_flag = False
        print("        ")
        print("        ")
        print("Enter 'exit' to leave program")
        revcol = input("Please select which collumn to reveal: ")
        if revcol == "exit": 
            print("Goodbye!")
            sys.exit()
        elif revcol not in selcol:
            print("        ")
            print("        ")
            print("ERROR:  Please enter a valid number.")
            hold()
            return getcollumn("R")
        return revcol
    if version == "F":
        place_flag = True
        print("        ")
        print("        ")
        print("Enter 'exit' to leave program")
        revcol = input("Please select which collumn to flag: ")
        if revcol == "exit":
            print("Goodbye!")
            sys.exit()
        elif revcol not in selcol:
            print("        ")
            print("        ")
            print("ERROR:  Please enter a valid number.")
            hold()
            return getcollumn("F")
        return revcol


def reveal(row, collumn, version):
    if newlist[row][collumn] == revealed[row][collumn]:
        print("Sorry! That is already revealed!")
        hold()
        main()
    if version == "R":
        newlist[row][collumn] = revealed[row][collumn]
        hold() 
    if version == "F":
        newlist[row][collumn] = "F"
        hold()
#tuple for what can be typed in input.
selrow = ('1', '2', '3', '4', '5')
selcol = ('1', '2', '3', '4', '5')
#makes newlist variable for the reason of being manipulated.
newlist = field

def getzero():
    '''
    this function is to find the coordinates to 
    '''
    for row in newlist:
        for column in newlist[row]:
            if column = 0

# holds the current field
def hold():
    print("            columns       ")                                          
    print("    ")                                                                 
    print("         1.  2.  3.  4.  5.   ")                                          
    print("    1.  ", newlist[0][0], "|", newlist[0][1], "|", newlist[0][2], "|", newlist[0][3], "|", newlist[0][4])  
    print("        --------------------")                   
    print(" r  2.  ", newlist[1][0], "|", newlist[1][1], "|", newlist[1][2], "|", newlist[1][3], "|", newlist[1][4])  
    print(" o      --------------------")                                              
    print(" w  3.  ", newlist[2][0], "|", newlist[2][1], "|" , newlist[2][2], "|", newlist[2][3], "|", newlist[2][4]) 
    print(" s      --------------------")                                              
    print("    4.  ", newlist[3][0], "|", newlist[3][1], "|" , newlist[3][2], "|", newlist[3][3], "|", newlist[3][4]) 
    print("        --------------------")                                              
    print("    5.  ", newlist[4][0], "|", newlist[4][1], "|" , newlist[4][2], "|", newlist[4][3], "|", newlist[4][4]) 

#makes the main program code for interacting with newlist.
def main():
#user inputs which row and collumn to reveal
    totalfield = field[0] + field[1] + field[2] + field[3] + field[4]
    if totalfield.count('M') > 0:
        print("Uh oh! You Blew Up!")
        sys.exit()
    revrow = getrow("R")
    if revrow == "F":
        revrow = getrow("F")
        flag = True
    else:
        flag = False
    if flag:
        revcol = getcollumn("F")
    elif not flag:
        revcol = getcollumn("R")
    revrow = int(revrow)-1
    revcol = int(revcol)-1
    mines_left = 0
    
    for i in range(len(field)):
        for collumns in field[i]:
            if collumns == '#' or collumns == 'F':
                mines_left += 1
    if mines_left == 4:
        print("Horray! You Won!")
        sys.exit()
    if not flag:
        reveal(revrow, revcol, "R")
    else:
        reveal(revrow, revcol, "F")
