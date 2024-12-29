# print 
print("Mensagem para o usuário final")

# input 
print("Olá " + input("Digite o seu nome: ") + "!")

# Desafio 1 
# Crie programa que o usuário digita o seu nome e retorna o número de caracteres 
nome = input("Digite o seu nome: ")
print(len(nome))

# Desafio 2 
# Crie um programa que o usuário digita 2 valores e retorna a soma 
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite um número: "))
print(valor1 + valor2)

# Desafio Bônus 
# Cálculo do Bônus 
nome_usuario = input("Digite o seu nome: ")
renda_usuario = int(input("Digite o valor da sua renda: "))
perc_bonus_usuario = float(input("Digite o percentual do bonus: "))

calculo_bonus = 1000 + renda_usuario + (renda_usuario * perc_bonus_usuario)

print(f"O usuário {nome_usuario} possui bonus de {calculo_bonus}")

