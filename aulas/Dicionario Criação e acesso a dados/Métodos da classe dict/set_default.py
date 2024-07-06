contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
contato  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}


# Setdefault sever para adicionar um valor ou chave caso não tenha ele adiciona 
# e se tive a chave e o valor ele não adiciona
