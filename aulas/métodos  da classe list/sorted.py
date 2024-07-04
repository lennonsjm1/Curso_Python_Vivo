linguagens = ["python", "js", "c", "java", "csharp"]
#basicamente a mesma coisa do Sort e [sorted] é uma função built-in já dentro da linguaguem
#Funções Built-in Python são funcionalidades pré-definidas e integradas na linguagem 

print(sorted(linguagens, key=lambda x: len(x)))

# E dentro dessa função tem a função Key e a função Reverse e a diferença que ele é uma função e a gente chame ele
# diferente do sort que é um elemento

print(sorted(linguagens, key=lambda x: len(x), reverse=True))