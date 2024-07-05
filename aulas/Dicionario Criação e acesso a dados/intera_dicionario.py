contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])
# É um jeito de percorre a o dicionario mais tem que direciona para algo espercífico
# Para ler o dicionario todo EX : colocar onde está armazenado mais [uma lista]

for chave, valor in contatos.items():
    print(chave, valor)
# desse jeito fica algo mais clear e simples com a função items 
