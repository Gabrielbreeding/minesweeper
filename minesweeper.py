#!/usr/bin/python3
#GabrielBreeding

'''a program where the user can interact with a list to reveal the lists true contents'''


#---------------imports------------------
import sys
import random as r


def makefield(field):
    '''
    A function to make the first 2 screens, the one the player sees, and the one the player sees after revealing.
    
    depending on the field (1 or 2),
    the function will return either the player's screen(1) or the revealed screen(2). 
    '''
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
maxbomb = 5
def placebomb(maxbomb):
    '''
    A function to place mines in the revealed field.
    
    The function continues until there are 4 bombs in the revealed field
    and selects a random x and y coordinate,
    the nested while loop checks to see if there is already a mine there,
    if there is, it selects a new random coordinate and repeats until it gets
    a new coordinate without a mine.
    '''
    #places the bombs
    bombs = 0
    maxbomb = 5
    while bombs < maxbomb:
        x = r.randint(0, 4)
        y = r.randint(0, 4)
        while revealed[y][x] == 'M':
            x = r.randint(0,4)
            y = r.randint(0,4)
        revealed[y][x] = 'M'
        bombs += 1
placebomb(maxbomb)

def placenums():
    '''
    A function that places the numbers you see in the program.
    
    The Function places the numbers depending on the amount of mines in it's detection radius.
    
    depending on the row and column,
    it will select different parts of the rows around it,
    and count the mines that it sees.
    
    visual:
    x is the coordinate.
    # is whats being detected.
    - is whats not being detected. 
    
        x|#|-       -|#|x       -|#|#       -|-|-       #|#|#
        #|#|-       -|#|#       -|#|x       #|#|-       #|x|#
        -|-|-       -|-|-       -|#|#       x|#|-       #|#|#
        
        #|x|#       -|-|-       -|-|-       #|#|-
        #|#|#       -|#|#       #|#|#       x|#|-
        -|-|-       -|#|x       #|x|#       #|#|-
    '''
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
        '''
        
        '''
placenums()

def getrow(version):
    '''
    A function that obtains a row number from the user.
    
    getrow(version)
    
    Versions are "R" or "F"
    
    Version "R" (For Revealing):
    the user can input the word "flag" to switch to version "F",
    the program will ask the user to pick a row to reveal from.
    
    Version "F" (For Flagging):
    the user can input the word "back" to switch back to version "R"
    the program will ask the user to pick a row to flag.
    
    if ever the user decides they want to quit the game, they can type "exit",
    and the program will end. if the user types a row that's out of range, 
    the program will give an error and have the user try again.
    '''
    if version == "R":
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
            screen()
            return getrow("R")
        return revrow
    if version == "F":
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
            screen()
            return getrow("F")
        return revrow

def getcollumn(version):
    '''
    A Function that gets a column from the user.
    
    
    getcollumn(version)
    
    version "R"
    '''
    if version == "R":
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
            screen()
            return getcollumn("R")
        return revcol
    if version == "F":
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
            screen()
            return getcollumn("F")
        return revcol


def reveal(row, collumn, version):
    '''
    A function that picks out the position the player called, and changes it.
    
    reveal(row, collumn, version)
    
    rows are 1-5
    collumns are 1-5
    version is "R" or "F"
    
    version "R"
        tells function that this is "Regular", 
        and it's just replacing things with numbers
        
    version "F"
        tells function that the user wants to place a flag,
        so the function will replace the coordinate with a "F"
        meaning that the coordinate is "Flagged"
        
    if a coordinate is already revealed or is "Flagged",
    then it will not reveal it.
    '''
    if newlist[row][collumn] == revealed[row][collumn]:
        print("Sorry! That is already revealed!")
        screen()
    if newlist[row][collumn] == "F" and version == "R":
        print("Sorry! That's flagged!")
    elif newlist[row][collumn] == "F" and version == "F":
        newlist[row][collumn] == "#"
        screen()
    elif version == "R":
        newlist[row][collumn] = revealed[row][collumn]
        screen() 
    elif version == "F":
        newlist[row][collumn] = "F"
        screen()
#tuple for what can be typed in input.
selrow = ('1', '2', '3', '4', '5')
selcol = ('1', '2', '3', '4', '5')
#makes newlist variable for the reason of being manipulated.
newlist = field

# screens the current field
def get_row(y):
    '''
    A function that will get a full specified row.
    '''
    if y == 0:
        row = "  r  " + str(y + 1) + " "
    elif y == 1:
        row = "  o  " + str(y + 1) + " "
    elif y == 2:
        row = "  w  " + str(y + 1) + " "
    elif y == 3:
        row = "  s  " + str(y + 1) + " "   
    else:
        row = "     " + str(y + 1) + " "  
        
    for i in range(len(newlist[y])):
        if i == 0:
            row += newlist[y][0]
        else:
            row += "|" + newlist[y][i] 
    return row
    
def screen():
    '''
    A function that prints out the screen that the player can see.
    
    it selects points from the matrix one at a time and prints them, putting |s in the middle of them.
    '''
    columns = "       "
    divider = "       "
    for i in range(len(newlist[0])): 
        columns += str(i+1) + " "
        divider += "--"    
        
    print("        columns       ")                                          
    print("    ")
    print(columns)
    for i in range(len(newlist)):
        print(get_row(i))

    
#makes the main program code for interacting with newlist.
if __name__ == "__main__":
    def main(maxbomb):
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
        
       
        if not flag:
            reveal(revrow, revcol, "R")
        else:
            reveal(revrow, revcol, "F")
        for i in range(len(field)):
            for collumns in field[i]:
                if collumns == '#' or collumns == 'F':
                    mines_left += 1
        if mines_left == maxbomb:
            print("Horray! You Won!")
            sys.exit()            
    screen()
    main(maxbomb)


