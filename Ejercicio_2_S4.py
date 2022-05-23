#mostrar todos los números impares desde un número de inicio y otro final.

numInicial = int(input('Ingrese el numero inicial: '))
numFinal = int(input('Ingrese el numero Final: '))

numerosImpar = []

while numFinal <= numInicial:
    numFinal = int(input('El segundo número debe ser mayor que el primero. Inroduce otro número: '))
for n in range(numInicial, numFinal + 1):
    if n % 2 != 0:
        numerosImpar.append(n)

print(f"Lista de Números impares entre {numInicial} y {numFinal}:")
print(numerosImpar)
