# Typing, listas e dicionários 

# TypeHint - informar o tipo de variavel 
# idade = 30 
# altura = 1.75

# idade: int = 30 
# altura: float = 1.75

# print(idade)

# Lista - ORDENADO
# produto = "sapato"
# produto_1 = "videogame"
# produto_3 = "vestido"

# carrinho = []

# carrinho.append(produto)
# carrinho.append(produto_1)   #extend permite incluir todos ao mesmo tempo
# carrinho.append(produto_3)

# print(carrinho)

# Dicionario - permite CHAVE VALOR
# produto_1 = { 
#     "nome":"Sapato",
#     "quantidade": 39,
#     "preco": 10.38, 
#     "disponibilidade": True
# }

# produto_2 = { 
#     "nome":"Sapato",
#     "quantidade": 35,
#     "preco": 10.45, 
#     "disponibilidade": True
# }

# carrinho = []

# carrinho.append(produto_1)
# carrinho.append(produto_2)

# print(carrinho)

# EXERCICIOS 
### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log_1 = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# log_2 = {'timestamp': '2021-06-24 10:00:00', 'level': 'NOT', 'message': 'NOT'}
# log_3 = {'timestamp': '2021-06-25 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# dicionario_logs = []

# dicionario_logs.append(log_1)
# dicionario_logs.append(log_2)
# dicionario_logs.append(log_3)


# print(dicionario_logs["level" == "ERROR"]) #mostra o primeiro log com registro de erro 

# logs_error = [log for log in dicionario_logs if log['level'] == 'ERROR']

# print(logs_error) # traz o registro de todos os logs contendo o erro 

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# list_numero = []
# list_numero.extend(range(0,9)) # inclusao de 0 a 8 

# numeros_pares = [numero for numero in list_numero if numero % 2 == 0]

# print(numeros_pares)

