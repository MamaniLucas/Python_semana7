a=0
b=1
n=int(input("ingrese el limite: "))
suma=0
for number in range(n):
    c=a+b
    a=b
    b=c
    print(b)
    suma += b
print("la suma es ", suma)
