import math
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c
def Subs(A,B):
    return [a-b for a,b in zip(A,B)]
def dotp(X,Y):
    return [a*b for a,b in zip(X,Y)]

    
A = list(map(int,raw_input().split()))
B = list(map(int,raw_input().split()))
C = list(map(int,raw_input().split()))
D = list(map(int,raw_input().split()))

AB = Subs(A,B)
BC = Subs(B,C)
CD = Subs(C,D)


X = cross(AB,BC)
Y = cross(BC,CD)

X1 = pow(X[0],2) + pow(X[1],2) + pow(X[2],2)
Y1 = pow(Y[0],2) + pow(Y[1],2) + pow(Y[2],2)
Phi = dotp(X,Y)
print Phi
print (math.sqrt(X1)*math.sqrt(Y1))



