#!/usr/bin/python3

# [[a, s, d] row 1?
#  [f, g, h] row 2?

#lists the first, unrevealed field.
field = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9'],
         ['10', '11', '12'],
         ['13', '14', '15']]

#lists the second, revealed field.
revealed = [["a", 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o']]

#prints the field for user to see.
print("field =", field)

#makes newlist variable for the reason of being manipulated.
newlist = field

def hold():
        print("1.", newlist[0])
        print("1.", newlist[0])
        print("2.", newlist[1])
        print("3.", newlist[2])
        print("4.", newlist[3])
        print("5.", newlist[4])
        main()


#makes the main program code for interacting with newlist.
def main():
    print("        ")
    print("        ")
    reveal = input("select which row to reveal: ")
    reveal = float(reveal)
#if everything is revealed, activate this.
    if newlist == revealed:
        print("all is revealed")
#if the input is 1, check if the first collumn is already revealed and then if not, reveal it.
    elif reveal == 1:
        if newlist[0] == revealed[0]:
            print("already revealed")
        else:
            newlist[0] = revealed[0]
            hold()
#if the input is 2, check if the second collumn is already revealed and if not, reveal it.
    elif reveal == 2:
        if newlist[1] == revealed[1]:
            print("already revealed")
        else:
            newlist[1] = revealed[1]
            hold()

    elif reveal == 3:
        if newlist[2] == revealed[2]:
            print("already revealed")
        else:
            newlist[2] = revealed[2]
            hold()

    elif reveal == 4:
        if newlist[3] == revealed[3]:
            print("already revealed")
        else:
            newlist[3] = revealed[3]
            hold()

    elif reveal == 5:
        if newlist[4] == revealed[4]:
            print("already revealed")
        else:
            newlist[4] = revealed[4]
            hold()



#loops the program
main()
