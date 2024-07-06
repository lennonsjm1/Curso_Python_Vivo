contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}

contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos.popitem()  # KeyError

# No Popitem não tendo o valor ele irá remover tudo em sequencia e no fim vai da um erro padrão
