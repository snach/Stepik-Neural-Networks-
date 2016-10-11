import numpy as np

X = np.array([[1, 60], [1, 50], [1, 75]])
print(X)
print("\n")

X_T = X.T
print(X_T)
print("\n")

XX_T = X_T.dot(X)
print(XX_T)
print("\n")

XX_T__1 = np.linalg.inv(XX_T)
print(XX_T__1)
print("\n")

XX_T__1X_T = XX_T__1.dot(X_T)
print(XX_T__1X_T)
print("\n")

Y = np.array([[10], [7], [12]])
print(Y)
print("\n")

B = XX_T__1X_T.dot(Y)
print(B)

