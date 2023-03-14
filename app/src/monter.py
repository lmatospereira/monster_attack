# -*- coding: UTF-8 -*-
mult = [[(x,y) for x in range(4)] for y in range(4)] 

for x in range(4):
    for y in range(4):
        print(mult[x][y], end=' ')
    print()