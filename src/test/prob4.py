import numpy as np

def prob4():
    m = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
    def det(m):
        print('det',m)
        def reduced(m, c):
            print('red',m)
            temp = m
            temp = temp[1:]
            for r in temp:
                r.pop(c)
            return temp
        sum = 0
        if len(m) > 2:
            for i in range(len(m)):
                sum += m[0][i]*det(reduced(m, i))
            return sum
        else:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    print(det(m))

if __name__=='__main__':
    prob4()
