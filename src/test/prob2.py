import numpy as np

def prob2():
    func = lambda t, y: t - y**2
    a = 0
    b = 2
    N = 10
    h = (b-a)/N
    t = np.arange(a, b, h)
    y = np.zeros(N)
    y[0] = 1
    for i in range(N-1):
        y[i+1] = y[i]+h*func(t[i]+h/2, y[i]+h*func(t[i], y[i])/2)
    print(y[-1])

if __name__=='__main__':
    prob2()
