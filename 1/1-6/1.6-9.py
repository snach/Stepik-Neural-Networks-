import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)
"""print("X:")
print(X)
print("Y: ")
print(Y)"""
Y_T = Y.T
#print("Y_T: ")
#print(Y_T)
try:
    XY_T = X.dot(Y_T)
    #print("XY_T:")
    print(XY_T)
except ValueError:
    print("matrix shapes do not match")


"""
2 3
5 9 9 10 8 9
3 4
6 11 3 5 4 5 3 2 5 8 2 2
"""
"""
2 3
8 7 7 14 4 6
4 3
5 5 1 5 2 6 3 3 9 1 4 6
"""