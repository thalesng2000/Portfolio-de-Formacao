import pandas as pd

dados = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

df = pd.read_csv(dados, encoding= "latin1", sep= ";")

# print(df.head(5)) #.head() escolhe as primeiras linhas
# print(df.tail(10)) #.head() escolhe as ultimas linhas

df_furto_celular_cisp = df.groupby("cisp")["furto_celular"].sum().reset_index()
                                                                  #.groupy é o código do pandas que agrupa as informações
                                                                  #para agrupar no parenteses é o qualitativo (que não pode somar)
                                                                  #para agrupar no colchetes é o quantitativo (que se pode somar)
                                                                  #.sum() soma o que está nos colchetes
print(df_furto_celular_cisp)

