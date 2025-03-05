import pandas as pd 
import os 
import glob

# Função que lê os documentos de JSON

# pasta_arquivos = [r"C:\Users\guilh\OneDrive\Documentos\Data Science\bootcamp_jornada\aula7_aprofundamento_funcoes.py\coleta_dia01.json",
#                   r"C:\Users\guilh\OneDrive\Documentos\Data Science\bootcamp_jornada\aula7_aprofundamento_funcoes.py\coleta_dia02.json",
#                   r"C:\Users\guilh\OneDrive\Documentos\Data Science\bootcamp_jornada\aula7_aprofundamento_funcoes.py\coleta_dia03.json"]
# #dados = pd.read_json(pasta_arquivos)
# print(dados)

# pasta = r"C:\Users\guilh\OneDrive\Documentos\Data Science\bootcamp_jornada\aula_7_2" # pasta dos arquivos
# arquivos_json = glob.glob(os.path.join(pasta,'*.json')) # partindo da biblioteca, pegar tudo com json
# df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
#print(df_list)

#concatenar os diversos df 
# df_total = pd.concat(df_list, ignore_index=True)
# print(df_total)


# Função Extração JSON
pasta = r"C:\Users\guilh\OneDrive\Documentos\Data Science\bootcamp_jornada\aula_7_2" # pasta dos arquivos 

def extrair_dados(pasta): 
    arquivos_json = glob.glob(os.path.join(pasta,'*.json')) # partindo da biblioteca, pegar tudo com json
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True) #ignore cria um novo indice
    return df_total

teste = extrair_dados(pasta) # Para teste, em produção apagar 


# Função de transformação 

def calcular_kpi_total_vendas (df): 
    teste["Total"] = teste["Quantidade"] * teste["Venda"]
    return df 

teste_1 = print(calcular_kpi_total_vendas(teste))

# Carregar base para CSV 

def carregar_dados(df, format_saida):
    for formato in format_saida:
        if formato == 'csv': 
            df.to_csv("dados.csv")

formato_de_saida = "csv"
carregar_dados(teste_1 , formato_de_saida)

