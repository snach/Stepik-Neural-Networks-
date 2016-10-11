import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
#fname = "https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
#print(data)
Y = data.T[:1].T
#print(Y)
ones = np.ones_like(Y)
cutX = data.T[1:].T
X = np.hstack((ones, cutX))


X_T = X.T
#print(X_T)
#print("\n")

XX_T = X_T.dot(X)
#print(XX_T)
#print("\n")

XX_T__1 = np.linalg.inv(XX_T)
#print(XX_T__1)
#print("\n")

XX_T__1X_T = XX_T__1.dot(X_T)
#print(XX_T__1X_T)
#print("\n")

B = XX_T__1X_T.dot(Y)
#print(B)

print(" ".join(map(str, B.flatten())))
