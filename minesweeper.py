#!/usr/bin/python3
#GabrielBreeding

'''a program where the user can interact with a list to reveal the lists true contents'''


#---------------imports------------------
import sys
import random as r

#lists the first, unrevealed field.
field = [['#' , '#' , '#', '#', '#'],
         ['#' , '#' , '#', '#', '#'],
         ['#' , '#' , '#', '#', '#'],
         ['#' , '#' , '#', '#', '#'],
         ['#' , '#' , '#', '#', '#']]

#lists the second, revealed field.
revealed = [['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-']]


#places the bombs
bombs = 0
while bombs < 5:
    x = r.randint(0, 4)
    y = r.randint(0, 4)
    revealed[y][x] = 'M'
    bombs += 1
c = 0
cc = 0
for box in revealed:
    for boxes in revealed[c]:
        if c == 0:
            if cc > 0 and cc < 4:
                middle = revealed[c][cc-2:3].count('M')
                bottom = revealed[c+1][cc-2:3].count('M')
                tM = (middle + bottom) 
            elif cc == 0:
                middle = revealed[c][:2].count('M')
                bottom = revealed[c+1][:2].count('M')
                tM = (middle + bottom)  
            elif cc == 4:
                middle = revealed[c][cc-2:3].count('M')
                bottom = revealed[c+1][cc-2:3].count('M')
                tM = (middle + bottom)
        elif c == 4:
            if cc > 0 and cc < 4:
                top = revealed[c-1][cc-2:3].count('M')
                middle = revealed[c][cc-2:3].count('M')
                tM = (top + middle)
            elif cc == 0:
                top = revealed[c-1][:2].count('M')
                middle = revealed[c][:2].count('M')
                tM = (top + middle)
            elif cc > 0 and cc < 4:
                top = revealed[c-1][3:].count('M')
                middle = revealed[c][3:].count('M')
                tM = (top + middle)                
        elif c > 0 and c < 4:
            if cc > 0 and cc < 4:
                top = revealed[c-1][cc-2:3].count('M')
                middle = revealed[c][cc-2:3].count('M')
                bottom = revealed[c+1][cc-2:3].count('M')
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
        revealed[c][cc] = tM 
        cc += 1
c += 1
            

#tuple for what can be typed in input.
selrow = ('1', '2', '3', '4', '5')
selcol = ('1', '2', '3', '4', '5')
#makes newlist variable for the reason of being manipulated.
newlist = field

# holds the current field
def hold():
    print("            columns       ")                                            # keep the same.
    print("    ")                                                                  # keep the same.
    print("         1.  2.  3.  4.  5.   ")                                            # keep the same.
    print("    1.  ", newlist[0][0], "|", newlist[0][1], "|", newlist[0][2], "|", newlist[0][3], "|", newlist[0][4]) # for i in range(4):
    print("        --------------------")                                              # print("    " + i+1 + ".  ", newlist[i][0], " | ", newlist[i][1], " | ", newlist[i][2]
    print(" r  2.  ", newlist[1][0], "|", newlist[1][1], "|", newlist[1][2], "|", newlist[1][3], "|", newlist[1][4]) # 
    print(" o      --------------------")                                              #
    print(" w  3.  ", newlist[2][0], "|", newlist[2][1], "|" , newlist[2][2], "|", newlist[2][3], "|", newlist[2][4]) #
    print(" s      --------------------")                                              #
    print("    4.  ", newlist[3][0], "|", newlist[3][1], "|" , newlist[3][2], "|", newlist[3][3], "|", newlist[3][4]) #
    print("        --------------------")                                              #
    print("    5.  ", newlist[4][0], "|", newlist[4][1], "|" , newlist[4][2], "|", newlist[4][3], "|", newlist[4][4]) #
    main()

#makes the main program code for interacting with newlist.
def main():
#user inputs which row and collumn to reveal
    totalfield = field[0] + field[1] + field[2] + field[3] + field[4]
    if totalfield.count('M') > 0:
        print("Uh oh! You Blew Up!")
        sys.exit()
    print("        ")
    print("        ")
    print("Enter 'exit' to leave program")
    revrow = input("Please select which row to reveal: ")
    if revrow == "exit":
        print("Goodbye!")
        sys.exit()
    elif revrow not in selrow:
        print("        ")
        print("        ")
        print("ERROR:  Please enter a valid number.")
        hold()
        main()
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
        main()

    revcol = int(revcol)-1
    revrow = int(revrow)-1
#if everything is revealed, activate this.
    if newlist == revealed:
        print("all is revealed")
        print("thanks for playing!")
        sys.exit()
    elif newlist[revrow][revcol] == revealed[revrow][revcol]:
        print("Sorry! That is already revealed!")
        main()
    else:
        newlist[revrow][revcol] = revealed[revrow][revcol]
        hold()
#for i in range(5):
 #   print("   ", i+1,  ".  ", newlist[i][0], " | ", newlist[i][1], " | ", newlist[i][2])
  #  if i < 4:
   #     print("        -----------------")
hold()
#loops the program
main()
