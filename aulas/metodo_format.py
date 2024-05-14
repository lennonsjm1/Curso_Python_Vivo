nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Guilherme", "idade": 28, "profissao": "Programador", "linguagem": "Python"}
print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} \ne estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))


print("Olá me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} \ne estou matriculado no curso de {0}.".format(linguagem, profissao,idade, nome))


print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} \ne estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Esse modo é de lista
print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} \ne estou matriculado no curso de {linguagem}.".format(**pessoa))