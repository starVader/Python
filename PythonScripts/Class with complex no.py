# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
class Complex:
    def __init__(self,real,imag):
        self.r = real
        self.i = imag
    def __add__(obj1,obj2):
        realr = obj1.r + obj2.r 
        imagr = obj1.i + obj2.i
        print "%.2f+%.2fi" % (realr,imagr)

    def __sub__(obj1,obj2):
        realr = obj1.r - obj2.r 
        imagr = obj1.i - obj2.i
        if imagr < 0:
            print "%.2f%.2fi"% (realr,imagr)
        else:
            print "%.2f+%.2fi " % (realr,imagr)
    
    def __mul__(obj1,obj2):
        realr = (obj1.r * obj2.r) - (obj1.i * obj2.i) 
        imagr = (obj1.r * obj2.i) + (obj2.r * obj1.i) 
        print "%.2f+%.2fi" % (realr,imagr)
        
    def __div__(obj1,obj2):
         z = complex(obj2.r,obj2.i)
         conj = z.conjugate()
         z1 = complex(obj1.r,obj1.i)
         num = z1 * conj
         den = z * conj
         result = num/den 
         if result.imag < 0:
            print "%.2f%.2fi"% (result.real,result.imag)
         else:
            print "%.2f+%.2fi " % (result.real,result.imag)
    def mod(self,real,imag):
        k = complex(real,imag)
        x2 = pow(k.real,2)
        y2 = pow(k.imag,2)
        z = x2+y2
        z = math.sqrt(z)
        print "%.2f+%.2fi " % (z.real,z.imag)
    
         
r1,i1 = map(int,raw_input().split())
r2,i2 = map(int,raw_input().split())
x = Complex(r1,i1)
x1 = Complex(r2,i2)



x+x1
x-x1
x*x1
x/x1
x.mod(r1,i1)
x1.mod(r2,i2)
