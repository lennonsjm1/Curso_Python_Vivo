def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("terça-feira, 16 de julho de 2024", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

# *args / **kwargs podem se qualquer valor ou qualquer coisa depois do " * "

# diferença entre eles que o args vem como uma dupla e o kwargs vem como dicionario

# O que é uma tupla em Python?
# Uma tupla ( tuple ) em Python é uma sequência imutável de valores de 
# qualquer tipo. Para criar uma tupla, lista-se uma sequência de valores 
# separados por vírgulas e, opcionalmente, entre parênteses. Tuplas são 
# úteis para representar registros (mas sem atribuir nomes aos campos).