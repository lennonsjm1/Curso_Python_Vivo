conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado) # todos elementos em B tem em A

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado) # todos elementos em A tem em B