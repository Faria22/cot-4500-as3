import numpy as np

def prob1():
    func = lambda t, y: t - y**2
    a = 0
    b = 2
    N = 10
    t = np.arange(a, b, b/10)
    y = np.zeros(N)
    y[0] = 1
    for i in range(N-1):
        y[i+1] = y[i]+(b/N)*func(t[i], y[i])
    print(y[-1])

if __name__=='__main__':
    prob1()
