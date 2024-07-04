numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)
#se passa um valor ele discarta e se passa um valor que não tem no conjuto ele fica de boa sem da um erro
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}