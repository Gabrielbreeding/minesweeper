#!/usr/bin/python3

# [[a, s, d] row 1?
#  [f, g, h] row 2?
field = [[1, 2, 3],
         [4, 5, 6]]
    
revealed = [["a", 'b', 'c'], 
            ['d', 'e', 'f']]

print("field =", field)
print("field[1] =", field[1])

newlist = field


def main():
    print("        ")
    print("        ")
    reveal = input("select which row to reveal: ")
    reveal = float(reveal)

    if newlist == revealed:
        print("all is revealed")

    elif reveal == 1:
        if newlist[0] == revealed[0]:
            print("already revealed")
        else:
            newlist[0] = revealed[0]
            print("1.", newlist[0])
            print("2.", newlist[1])

    elif reveal == 2:
        if newlist[1] == revealed[1]:
            print("already revealed")
        else:
            newlist[1] = revealed[1]
            print("1.", newlist[0])
            print("2.", newlist[1])
    main()
main()
