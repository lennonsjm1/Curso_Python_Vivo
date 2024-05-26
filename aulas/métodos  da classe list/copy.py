lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

#Método copy, por mais que uma copia da outra são objetos diferentes 
#o que tu faz no l2 não reflete no l1 


l2[0] = 2

print(l2)
print(lista)