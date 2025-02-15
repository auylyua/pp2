import math
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
s=((a*n*a)/4)*(1/(math.tan(math.pi/n)))
print("The area of the polygon is: "+str(s)+"cm²")