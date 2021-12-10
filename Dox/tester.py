
import numpy as np

def main():

    b = 1
    m = 1
    k = 1
    A = np.matrix([[-b / m, -k / m], [1, 0]])
    B = np.eye(A.shape[0], A.shape[1])
    pass



if __name__ == '__main__':
    main()


