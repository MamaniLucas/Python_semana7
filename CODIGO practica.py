pares=0
impares=0
positivos=0
negativos=0
neutros=0
limite=5
for i in range(limite):
    number =int(input("ingrese el numero: "))
    if number %2==0:
       pares +=1
    else:
       impares +=1
    if i>0:
        positivos +=1
    else:
        negativos +=1
    if i==0:
        neutros +=1
print("la cantidad de numeros pares es : ", pares)
print("la cantidad de numeros impares", impares)
print("la cantidad de numeros positivos es ", positivos)
print("la cantidad d numeros negativos es  ", negativos)
print("la cantidad de numeros neutros ", neutros)
