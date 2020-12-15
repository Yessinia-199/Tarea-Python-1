import math
print ("Teniendo la ecuación ax^2 + bx + c")
print("-------")
a = int(input("ingrese el valor de a:"))
b = int(input("ingrese el valor de b:"))
c = int(input("ingrese el valor de c:"))

x= (b*b)- 4*a*c

if x<0:
    print ("No existe soluciones reales")
else:
    x1 = (-b + (x**(1/2)))
    x2 = (-b + (x**(1/2)))

print("--- soluciones---")
print("Solucion x1:", x1)
print("solucion x2:", x2)