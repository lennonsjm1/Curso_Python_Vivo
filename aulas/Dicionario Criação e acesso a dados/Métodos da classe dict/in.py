contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

email = "guilherme@gmail.com" in contatos  # True
print(email)

email = "megui@gmail.com" in contatos  # False
print(email)

idade = "idade" in contatos["guilherme@gmail.com"]  # False
print(idade)

fone = "telefone" in contatos["giovanna@gmail.com"]  # True
print(fone)


# Ajuda a verifica se operado está em uma sequencia 

