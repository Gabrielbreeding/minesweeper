#!/usr/bin/python3

# [[a, s, d] row 1?
#  [f, g, h] row 2?
field = [[1, 2, 3],
         [4, 5, 6]]
    
revealed = [["a", 'b', 'c'], 
            ['d', 'e', 'f']]

print("field =", field)
print("field[1] =", field[1])

row1 = field[0]
row2 = field[1]




def interact():
    print("1.", row1) 
    print("2.", row2)    
    
    reveal = input("select which row to reveal: ")
    reveal = float(reveal)    
    
    if reveal == 1 and row1 == revealed[0] or reveal == 2 and row2 == revealed[1]:
        print("already revealed")
    
    elif reveal == 2 and row2 == true:
        print("already revealed")

    elif reveal == 1 and row2 == true or reveal == 2 and row1 == true:
    
        print("1.", revealed[0])
        print("2.", revealed[1])

    elif reveal == 1:
        row1 = revealed[0]
        print("1.", row1)
        print("2.", row2)
    
    
    elif reveal == 2:
        print("1.", field[0])
        print("2.", revealed[1])
        row2 == true
interact()    
