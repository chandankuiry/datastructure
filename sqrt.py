from __future__ import division
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root
k=int(input("type an integer"))
n=squareroot(k)
print"square root of",k ,"is",n
 

