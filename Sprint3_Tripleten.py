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



'''LIÇÃO 4 - Olhando para os nossos dados'''

