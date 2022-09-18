import numpy as np
def check_input(test):
    r=0
    c=0
    for i in range(0,len(test[0])):
        for j in range(1,len(test[0])):
            if(test[i][0]==test[i][j] or type(test[j][i])==str):
                r=r+1
                
    for i in range(0,3):
        for j in range(1,3):
            if(test[0][j]==test[i][j] or type(test[i][j])==str):
                   c=c+1
    if(r==0 and c==0):
        return True
    else:
        return False

test1 = [[1, 2, 3],
        [2, 3, 1],
        [3, 1, 2]]

test2 = [[1, 2, 3, 4],
        [2, 3, 1, 3],
        [3, 1, 2, 3],
        [4, 4, 4, 4]]

test3 = [['a', 'b', 'c'],
        ['b', 'c', 'a'],
        ['c', 'a', 'b']]

print(check_input(test1)) # must return true
print(check_input(test2)) # must return false
print(check_input(test3)) # must return false
