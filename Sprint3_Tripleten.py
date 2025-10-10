'''SPRINT 3

CAPÍTULO 2 - LEITURA E VISUALIZAÇÃO DE DADOS


LIÇÃO 2 - Como resolver problemas com arquivos CSV

Tarefa 1
Um conjunto de dados está disponível em /datasets/letters_colors_decimals.csv.  Os valores nesse conjunto estão separados por $, e a é usado como ponto decimal.

Leia-o de forma que:

A primeira linha se torne o cabeçalho;
As colunas sejam separadas corretamente;
Os decimais sejam lidos corretamente.
Imprima o DataFrame.'''

import pandas as pd

df = pd.read_csv('/datasets/letters_colors_decimals.csv', sep='$', decimal='a')

print(df)


'''LIÇÃO 3 - Como ler arquivos do Excel

Tarefa 1
Calcule a pontuação média das avaliações seguindo estas etapas:

Leia a primeira planilha do arquivo Excel localizado em /datasets/product_reviews.xlsx e armazene-a em uma variável chamada df_reviews.
Selecione a coluna 'review' em df_reviews.
Aplique o método apropriado para calcular o valor médio.
Imprima o resultado na tela.'''

import pandas as pd

df_reviews = pd.read_excel('/datasets/product_reviews.xlsx')

print(df_reviews['review'].mean())


'''Tarefa 2
Para obter mais informações sobre os produtos nesse conjunto de dados, leia a planilha products do arquivo Excel em uma variável chamada df_products.

Em seguida, classifique o DataFrame pela coluna 'id' em ordem crescente usando o método apropriado e armazene-o na variável sorted_df_products. Se você não conseguir lembrar o nome do método, não se preocupe: temos uma dica que vai ajudar.

Por fim, não se esqueça de imprimir o DataFrame classificado.'''

import pandas as pd

df_products = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name = 'products') # escreva seu código aqui

sorted_df_products = df_products.sort_values(by='id')# escreva seu código aqui

print(sorted_df_products)


'''Tarefa 3
Além dos nomes dos produtos, o conjunto de dados também contém informações sobre como os produtos são categorizados. Por isso havia uma coluna 'category_id' na tabela da última tarefa.

Leia a última planilha, product_categories, em uma variável chamada df_categories. Em seguida, basta imprimir df_categories na tela.'''

import pandas as pd

df_categories = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name = 'product_categories')# escreva seu código aqui

print(df_categories)



'''LIÇÃO 4 - Olhando para os nossos dados

Tarefa 1
O pré-código já inclui código para imprimir as primeiras 5 linhas do conjunto de dados de usinas usando o método head(). Escreva um código que:

tenha uma amostra de 5 linhas aleatórias do conjunto de dados e as armazene na variável sample. Use random_state=543210 para a amostragem.
imprima a variável sample.
'''
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.head())
print()

sample = data.sample(5,random_state=543210)# escreva seu código aqui
print(sample)


'''Tarefa 2
Agora que temos uma noção de como são os dados em cada coluna, confira a informação geral sobre esse conjunto de dados chamando o método info(). Incluímos o código da última tarefa para que você possa comparar lado a lado as linhas da amostra com o resultado de info().'''

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

sample = data.sample(5, random_state=543210)
print(sample)
print()

data.info()



'''LIÇÃO 5 - Descrições numéricas e Describe()


Tarefa 01
Obtenha uma visão geral apenas da coluna 'primary_fuel' chamando describe() nela e imprimindo o resultado. O conjunto de dados já foi lido corretamente para você no pré-código.
'''
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data['primary_fuel'].describe())


'''
Tarefa 02
No resultado da tarefa anterior, descobrimos que existem 15 valores únicos na coluna 'primary_fuel'. Vamos verificar isso agora. Para fazer isso, chame o método nunique() nessa coluna. Atribua o resultado a uma variável chamada unique e imprima-a na tela.
'''
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

unique = data['primary_fuel'].nunique()# escreva seu código aqui
print(unique)


'''Tarefa 03
Agora verifique se o valor mais comum na coluna 'primary_fuel' realmente é 'Solar'. Para fazer isso:

Filtre o DataFrame original, extraindo apenas as linhas em que 'primary_fuel' é igual a 'Solar' e armazene-o na variável solar_data.
Verifique a forma do DataFrame obtido e o armazene na variável solar_shape.
Imprima a variável.
'''
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

solar_data = data[data['primary_fuel'] == 'Solar']# escreva seu código aqui
solar_shape = solar_shape = solar_data.shape# escreva seu código aqui
print(solar_shape)




'''CAPÍTULO 3 - TRATAMENTO DE VALORES AUSENTES E DUPLICADOS


LIÇÃO 2 - Contagem de valores ausentes

Nunca é uma má ideia chamar info() em um novo conjunto de dados. Vamos verificar isso no DataFrame dos logs dos visitantes, que associamos a uma variável chamada df_logs:
'''
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

print(df_logs.info())


'''Qual método aprendemos no sprint de Python básico para encontrar e contar valores ausentes?
'''
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs.isna().sum())


'''Vamos chamá-lo na coluna 'source' do DataFrame, incluindo os valores ausentes:
'''
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs['source'].value_counts(dropna=False))


'''Tarefa 1
Aplique o método value_counts() à coluna 'email' e armazene o resultado na variável email_values. Dessa vez, não inclua os valores ausentes no resultado. Imprima o resultado.
'''
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

email_values = df_logs['email'].value_counts() # escreva seu código aqui

print(email_values)


'''Tarefa 2
Agora vamos tentar ordenar os resultados por índice, e não por valor, para ver se isso acrescenta algum significado aos valores da coluna 'email'. Reescreva a variável email_values usando a ordenação e imprima o resultado.
'''
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

email_values = df_logs['email'].value_counts()
email_values = df_logs['email'].value_counts().sort_index() # escreva seu código aqui

print(email_values)


'''LIÇÃO 03 - Filtragem de DataFrames para lidar com valores ausentes

'''



