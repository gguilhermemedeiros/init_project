# TEORIA
import math 
import pandas as pd 
import numpy as np 

# Na classe de string temos algumas funções específicas para esta classe 
#nome = "Guilherme" 
#print(nome.lower()) # transforma tudo em minusculo
#print(nome.upper()) # transforma tudo em maiusculo 
#print(math.pi)

# TypeError: erro de tipo, ou seja, quando utilizamos tipos de variáveis em funções de tipos diferentes 
#try: 
    #resultado = len(3)
    #print(resultado)
#except TypeError as e: 
    #print(e)

# Checar se a variavel e do tipo correto 
# numero = int(input("Insira um numero"))
# if isinstance (numero,int): 
#     print("É UM NUMERO INTEIRO")
# else: 
#     print("A variável nao é inteiro")

# PRÁTICA 
#### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_1 = int(input("Forneça um numero: "))
# numero_2 = int(input("Forneça um numero: "))
# print(numero_1 + numero_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# dividendo = 5 
# numero_1 = int(input("Forneça um numero: "))
# print(numero_1 % dividendo)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_1 = int(input("Forneça um numero: "))
# numero_2 = int(input("Forneça um numero: "))
# print(numero_1 * numero_2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_1 = int(input("Forneça um numero: "))
# numero_2 = int(input("Forneça um numero: "))
# print(numero_1 / numero_2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero_1 = int(input("forneca um numero: "))
# print(numero_1 ** 2 )

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input("Forneça um numero: "))
# numero_2 = float(input("Forneça um numero: "))
# print(numero_1 + numero_2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input("Forneça um numero: "))
# numero_2 = float(input("Forneça um numero: "))
# lista = [numero_1,numero_2]
# print(np.mean(lista))

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero_1 = int(input("Forneça um numero base: "))
# numero_2 = int(input("Forneça um numero de expoente: "))
# print(numero_1 ** numero_2)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temp_celsius = float(input("Qual a temperatura em celsius: "))
# temp_farh = temp_celsius * 1.8 + 32 
# print(temp_farh)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Qual a tamanho do raio: "))
# area_circulo = math.pi * (raio ** 2) 
# print(area_circulo) 

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = input("Escreva um texto: ")
# print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# texto = input("Escreva seu nome: ")
# print(texto.lower())

