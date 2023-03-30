import numpy as np

def prob6():
    m = [[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]]
    val = np.linalg.eigvals(m)
    print(val)

if __name__=='__main__':
    prob6()
