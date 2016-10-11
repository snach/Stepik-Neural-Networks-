perfect = False
#     x0  x1  x2  ^y
ex1 = [1, 1, 0.3, 1]
ex2 = [1, 0.4, 0.5, 1]
ex3 = [1, 0.7, 0.8, 0]
w = [0, 0, 0]


def iteration(ex):
    sum = w[0]*ex[0] + w[1]*ex[1] + w[2]*ex[2]
    if sum > 0:
        Y = 1
    else:
        Y = 0
    print("Y: " + str(Y))
    print("ex[3]: " + str(ex[3]))
    if Y != ex[3]:

        if Y == 0:
            w[0] += ex[0]
            w[1] += ex[1]
            w[2] += ex[2]
        if Y == 1:
            w[0] -= ex[0]
            w[1] -= ex[1]
            w[2] -= ex[2]


iteration(ex1)
print(w)
iteration(ex2)
print(w)
iteration(ex3)
print(w)





