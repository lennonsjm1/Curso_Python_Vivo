contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#contatos["chave"]  # KeyError
# Sem o metodo get o sistema para e da KeyError significa que a chave que procura não tem dentro do dicionario e para o programa


resultado = contatos.get("chave")  # None
print(resultado)
# Esse método para verificação de chaves dentro do dicionário e se por acaso não ter ele retorna " None "

resultado = contatos.get("chave", {})  # {}
print(resultado)
# Mesma coisa do exemplo anterio mais você da uma condição se por acaso não tiver a chave procurada e se não tiver 
# ele retornara {}

resultado = contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)


# O método get serve para verificação de chaves dentro do dicinário sem essa verificação o sistema para.
