from urllib.request import urlopen
import numpy as np
#s = "https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"
#f = urlopen(s)
#print(f)
f = urlopen(input())
mat = np.loadtxt(f, skiprows=1, delimiter="," )
#print(mat)
print(mat.mean(axis=0))
