import numpy as np

def prob3():
    m = [[2,-1,1,6],[1,3,1,0],[-1,5,4,-3]]
    n = len(m)
    x = np.zeros(n)
    for k in range(n):
        for j in range(k+1,n):
            c = m[j][k]/m[k][k]
            for i in range(4):
                m[j][i] = m[j][i]-c*m[k][i]

    x[-1] = m[-1][-1]/m[-1][-2]
    for i in reversed(range(n-1)):
        sum = 0
        for j in range(i+1, n):
            sum += m[i][j]*x[j]
        x[i] = (m[i][n]-sum)/m[i][i]

    print(x)


if __name__=='__main__':
    prob3()
