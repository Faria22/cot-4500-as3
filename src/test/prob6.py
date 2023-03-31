import numpy as np

def prob6():
    m = [[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]]
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
