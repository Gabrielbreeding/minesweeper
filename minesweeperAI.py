#!/usr/bin/python3
#GabrielBreeding
#11/22/19

import minesweeperAdapted as ms

z = []

def rr(x, y):
    '''
    This function will reveal everything in the radius of the coordinate provided.
    '''
    if x == 0:
        if y == 0:
            try:
                ms.reveal(x+1,y,"R")
            except:
                z
            try:
                ms.reveal(x+1,y+1,"R")
            except:
                z
            try:
                ms.reveal(x,y+1,"R")
            except:
                z
    
    if x > 0 and y > 0 and x < 4 and y < 4:     
        try:
            ms.reveal(x-1, y-1, "R")
        except:
            z
        try:
            ms.reveal(x-1, y, "R")
        except:
            z
        try:
            ms.reveal(x-1, y+1, "R")
        except:
            z
        try:
            ms.reveal(x, y-1, "R")
        except:
            z
        try:
            ms.reveal(x, y+1, "R")
        except:
            z
        try: 
            ms.reveal(x+1, y-1, "R")
        except:
            z
        try:
            ms.reveal(x+1, y, "R")
        except:
            z
        try:
            ms.reveal(x+1, y+1, "R")
        except:
            z

coordinate = ms.newlist
ms.hold()

#first, reveal something.
ms.reveal(0, 0, "R")
ms.hold

#second, if it's zero, reveal the area around it.
if coordinate[0][0] == 0:
    rr(0, 0)