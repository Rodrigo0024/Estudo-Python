usuario ={
    "nome": "João",
    "idade":28,
    "liguagem": "Python",
    "ativo": True
}
print(usuario["nome"])  # Acessa o valor associado à chave "nome"

meu_dicionario = {} #iniciando um dicionário vazio

outro_dicionario = dict(host="localhost", port=8080) #Usando o Construtor dict() com argumentos nomeados
print(outro_dicionario)  # Imprime o dicionário criado  


chaves = ["id", "nome", "idade"]
valores = [1, "João", 28]
dicionario =dict(zip(chaves,valores)) #Usando a função zip() para criar um dicionário a partir de duas listas
print(dicionario)  # Imprime o dicionário criado a partir das listas

print(usuario.get("idade"))  # Acessa o valor associado à chave "idade" usando o método get()
print(usuario.get("email", "Chave não encontrada"))  # Acessa o valor associado à chave "email" usando o método get() com valor padrão


usuario["email"] = "joao@example.com"  # Adiciona uma nova chave "email" ao dicionário
usuario["idade"] = 29  # Modifica o valor associado à chave "idade"
print(usuario)  # Imprime o dicionário atualizado

for chave, valor in usuario.items():  # Itera sobre os pares chave-valor do dicionário
    print(f"{chave}: {valor}")  # Imprime cada chave e seu valor correspondente