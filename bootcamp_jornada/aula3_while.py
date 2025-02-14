# Debug 
# Permite rodar blocos de códigos ao inves de rodar toda a aplicação, visando identificar bugs 

# CONTROLE DE FLUXO

# IF - estrutura condicional fundamental identificando ser True or False. Ordem importa.
# x = -3

# if x < 0: 
#     x = 0 
#     print("Negative chenged to zero")
# elif x == 0: 
#     print("Zero")
# elif x == 1: 
#     print("Single")
# else: 
#     print("More")

# FOR - útil para executar uma operação para cada elemento de uma coleção. Condição conhecida, sei quando parar 
# for i in range(1,5): 
#     print(i)

# lista_de_alunos = ["Guilherme","Joao","Carlos"]

# for nome in lista_de_alunos: 
#     print(nome)

# WHILE -> Condição desconhecida. Não sei por quanto tempo irá ficar rodando  
# dados = []
# entrada = ""

# while entrada.lower() != "sair": 
#     entrada = input("Digite um valor ou sair para terminar: ")
#     print("Coninuar")

# EXERCICIOS 
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# quantidade = 3
# preco = -20 

# if quantidade >= 0 and preco >= 0: 
#     print("Dados validos")
# elif quantidade < 0 or preco < 0: 
#     print("Dados Invalidos")

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# entrada = ""

# while entrada != "sair": 
#     entrada = input("forneça palavras")
#     print("Correto")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = ""

# while numero not in (5,10): 
#     numero = int(input("Forneça um numero: "))
#     print("Dados Inválidos")