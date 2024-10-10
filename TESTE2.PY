lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:  # Check if the number is even

        if item < 0:  # If even and negative
            lista_final.append('A')
    
        else:  # If even and non-negative
            lista_final.append('B')

    else:  # If the number is odd

        if item < 0:  # If odd and negative
            lista_final.append('C')
    
        else:  # If odd and non-negative
            lista_final.append('D')

print(lista_final)
