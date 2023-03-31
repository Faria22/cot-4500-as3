import numpy as np

def prob6():
    m = [[2,2,1],[2,3,0],[1,0,2]]
    n = len(m)
    val = np.linalg.eigvals(m)
    for v in val:
        if v < 0:
            print(False)
            return
    t = np.transpose(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != t[i][j]:
                print(False)
                return
    print(True)


if __name__=='__main__':
    prob6()
