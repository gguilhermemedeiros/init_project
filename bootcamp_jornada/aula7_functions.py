# Funções em Python: Compreensão, Uso e Prática 
# Uma das principais utilidades é a reutilização de código/processos 

# CRIAÇÃO DE FUNÇÃO 
# keyword def seguida do nome da função
# def funcao_hello_world(): 
#     return "HELLO, WORLD"

# print(funcao_hello_world())

# Função de soma 
valor_1 = 7 
valor_2 = 5

def somatoria(valor_1_para_somar, valor_2_para_somar): 
    """
    Função destinada a realizar soma a partir de dois valores fornecidos 
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

print(somatoria(valor_1,valor_2))





