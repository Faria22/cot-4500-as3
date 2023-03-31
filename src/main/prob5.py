import numpy as np

def prob5():
    m = [[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]]
    n = len(m)
    for i in range(n):
        sum = 0
        for j in range(n):
            if i == j:
                continue
            sum += m[i][j]
        if m[i][i] < sum:
            print(False)
            return
    print(True)

if __name__=='__main__':
    prob5()
