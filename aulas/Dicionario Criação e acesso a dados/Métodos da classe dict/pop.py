contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {})  # {} e se ela não existi ela retornara vazia nesta condição
print(contatos)

# O pop irá remover uma chave do seu dicionario