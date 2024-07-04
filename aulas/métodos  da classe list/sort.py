linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

#onde elemento sort retorna a lista aleatoriamente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)

#o elemento retorna aleatoriamente mais com a função reverse=True faz a lista aparece em ordem de trás pra frente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))

#aqui retorna por tamanho em ordem crescente e tem uma função anônima >[lambda] e o "X" é o elemento
#o len(x) tira o tamanho de uma string /// fazendo isso ele retorna por tamanho da strings

#a função  len tira o tamanho das coisas 

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)

#aqui é mesma coisa que codigo anterior mais com a função reverse=True ele retorna com a 
#ordem do maior para o menor
#em resumo ele faz o reverso do codigo anterior

#a função  len tira o tamanho das coisas 