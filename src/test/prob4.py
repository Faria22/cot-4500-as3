import numpy as np

def prob4():
    m = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
    def det(m):
        def reduced(m, c):
            temp = []
            for n, i in enumerate(m):
                temp.append([])
                for j in i:
                    temp[n].append(j)
            temp = temp[1:]
            for i in range(len(temp)):
                temp[i].pop(c)
            return temp
        sum = 0
        if len(m) > 2:
            for i in range(len(m)):
                sum += (-1)**i*m[0][i]*det(reduced(m, i))
            return sum
        else:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    def lower(matrix):
        m = []
        for n, i in enumerate(matrix):
            m.append([])
            for j in i:
                m[n].append(j)
        n = len(m)
        u = upper(m)
        l = np.zeros((n,n))
        for i in range(n):
            l[i][i] = 1
        for i in range(1, n):
            for j in range(i):
                diff = m[i][j]
                for k in range(j):
                    diff -= l[i][k]*u[k][j]
                l[i][j] = diff/u[j][j]
        return l

    def upper(matrix):
        m = []
        for n, i in enumerate(matrix):
            m.append([])
            for j in i:
                m[n].append(j)
        n = len(m)
        for k in range(n):
            for j in range(k+1,n):
                c = m[j][k]/m[k][k]
                for i in range(n):
                    m[j][i] = m[j][i]-c*m[k][i]
        return np.array(m)

    print(det(m), end='\n\n')
    print(lower(m), end='\n\n')
    print(upper(m))

if __name__=='__main__':
    prob4()
