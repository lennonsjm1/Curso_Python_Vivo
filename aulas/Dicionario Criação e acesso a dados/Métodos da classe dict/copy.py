contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"]  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}

# O método copy você pode copia um dicionario e amazena em outra 
# string e fazer alterações sem afeta a anterio