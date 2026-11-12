## Crie u dicionario

dicionario = {
    "nome": "Maria",
    "idade": 25
}

#imprimindo o dicionario

print(dicionario)  # Imprime o dicionário criado

#imprimando o valor associado à chave "nome"
print(dicionario["nome"])  # Acessa o valor associado à chave "nome"


#Crie um dicionario a partir de duas listas usando a função zip()


dicionario_1 = ["nome", "idade", "cidade"]
dicionario_2 = ["João", 30, "São Paulo"]


dicionario_zip = dict(zip(dicionario_1 , dicionario_2 ))  # Usando a função zip() para criar um dicionário a partir de duas listas

#acesse  o valor do dicionario usando a função get() e forneça um valor padrão caso a chave não exista
default_value = dicionario_zip.get("profissao", "Chave não encontrada")  # Acessa o valor associado à chave "profissao" usando o método get() com valor padrão
print(default_value)  # Imprime o valor padrão caso a chave não exista