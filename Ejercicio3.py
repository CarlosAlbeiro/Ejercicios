numero=[1,2,3,4,5,6]
copia=[]
contador=0
print("recorrer con el while")
while contador < len(numero):
    print(numero[contador])
    contador+=1

print("recorrer con el for")
for i in range(len(numero)):
    print(numero[i])

print("sumandole uno")
for i in range(len(numero)):
    print(numero[i]+1)

print("copia incrementada")
for i in range(6):
    copia.append(numero[i]+1)


print(numero)
print("copia: ",copia)

print("promedios")
suma1=0
suma2=0
for i in range(6):
    suma1=suma1+numero[i]
    suma2=suma2+copia[i]
print(suma1/6)
print(suma2/6)

