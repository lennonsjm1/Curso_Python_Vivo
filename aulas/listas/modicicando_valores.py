numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

#segundo modo eh de compreesão onde é uma maneira fácil e de ser usado 

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [quadrado ** 2 for quadrado in numeros]
print(quadrado)

