#!/usr/bin/python3
#GabrielBreeding

'''a program where the user can interact with a list to reveal the lists true contents'''


#---------------imports------------------
import sys


#lists the first, unrevealed field.
field = [['1' , '2' , '3'],
         ['4' , '5' , '6'],
         ['7' , '8' , '9'],
         ['10', '11', '12'],
         ['13', '14', '15']]

#lists the second, revealed field.
revealed = [["a", 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o']]
#makes newlist variable for the reason of being manipulated.
newlist = field

# holds the current field
def hold():
        print("            columns       ")
        print("    ")
        print("         1.    2.    3.   ")
        print("    1.", newlist[0][0], "  |  ", newlist[0][1], "  |  ", newlist[0][2])
        print("        ----------------")
        print(" r  2.", newlist[1])
        print(" o      ----------------")
        print(" w  3.", newlist[2])
        print(" s      ----------------")
        print("    4.", newlist[3])
        print("        ----------------")
        print("    5.", newlist[4])
        main()

#makes the main program code for interacting with newlist.
def main():
#user inputs which row and collumn to reveal
    print("        ")
    print("        ")
    revrow = input("Please select which row to reveal: ")
    if revrow == "exit":
        print("Goodbye!")
        sys.exit()
    print("        ")
    print("        ")
    revcol = input("Please select which collumn to reveal: ")
    if revcol == "exit":
        print("Goodbye!")
        sys.exit()
    revcol = int(revcol)-1
    revrow = int(revrow)-1
#if everything is revealed, activate this.
    if newlist == revealed:
        print("all is revealed")
    elif newlist[revrow][revcol] == revealed[revrow][revcol]:
        print("Sorry! That is already revealed!")
        main()
    else:
        newlist[revrow][revcol] = revealed[revrow][revcol]
        hold()
hold()
#loops the program
main()
