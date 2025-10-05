movies = {
    'Her': 2013, 
    'Big Eyes': 2014, 
    'Taxi Driver': 1976, 
    'The King of Comedy': 1982
}# crie um dicionário

print(movies)

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price = financial_info['Walmart']# Escreva seu código aqui
print(walmart_price)

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

nike_price = financial_info.get('Nike')# escreva o código aqui
print(nike_price)


financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

financial_info['Microsoft']=208.35# adicione um novo par aqui

print(financial_info)


'''Tarefa 1
A equipe de gestão ABC pediu que você reorganize a lista dos clientes de modo que eles possam acessar 
os dados com maior facilidade.

Seu objetivo é transformar cada lista da lista clients em um dicionário e então imprimir esse dicionário,
 antes de converter a próxima lista em um novo dicionário.

Use as seguintes chaves para cada dicionário que criar:
"id"
"client_name"
"age"
"yearly_income"
"work_field"'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]


for client in clients:
    client_info = {"id": client[0],
                   "client_name": client[1],
                   "age": client[2],
                   "yearly_income": client[3],
                   "work_field": client[4]}
    print(client_info)



'''TAREFA 02 - PRÁTICA CAPÍTULO 02
Desta vez, o departamento de marketing do ABC está interessado em saber o nível de renda para cada área
 de trabalho de seus clientes. Ele pediu para você coletar dados de renda dos clientes para cada área.

No pré-código, assim como na tarefa anterior, você vai ver a lista clients. Se você quiser dar mais uma 
olhada na lista, ela está aqui:'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

incomes_per_field = {}

for client in clients:
	field = client[4]
	income = client[3]
	if incomes_per_field.get(field) == None:
		incomes_per_field[field] = [income]
	else:
		incomes_per_field[field].append(income)
		
print(incomes_per_field)



'''Tarefa 1 - lição 4- cap3 - sprint2
No pré-código, você verá as funções que criamos nesta lição para filtrar os dados e imprimir o resultado.
 Use essas funções para filtrar filmes mais longos do que 140 minutos e imprima o resultado.'''

def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration:
            filtered_result.append(row)
    return filtered_result 

def print_movie_info(data):
    for movie in data:
        print(movie)

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

movies_filtered = filter_by_timing(movies_info, 140)# chame a função de filtragem aqui
print_movie_info(movies_filtered)




# essa função imprime a tabela filtrada. Não a modifique
def print_movie_info(data):
    for movie in data:
        print(movie)



'''Tarefa 2 - lição 4- cap3 - sprint2
Com base na função acima, escreva uma nova função filter_by_year() que vai filtrar os filmes por ano de 
lançamento. A nova função deve ter dois parâmetros:

data= — os dados dos filmes
year= — o critério de filtragem com base em um ano
A função deve retornar uma lista de listas que contenham apenas os filmes lançados após year='''

def filter_by_year(data,year):
    movies_filtered = []
    for movie in data:
        if movie[2] > year:
            movies_filtered.append(movie)
    return movies_filtered# defina sua função filter_by_year() aqui

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# abaixo há duas chamadas das funções: uma para filtrar os dados e outra para imprimir o resultado
movies_filtered = filter_by_year(movies_info, 1990)
print_movie_info(movies_filtered)


'''Tarefa 1 - lição prática - cap3 - springt2
Vamos começar escrevendo uma função chamada filter_clients para filtrar a lista de clientes por área de 
trabalho. A função vai receber dois parâmetros: clients_list (a lista de clientes) e field (o campo com a
 área de trabalho que a função precisa encontrar). A função vai iterar sobre cada cliente na lista, e se 
 ela encontrar o cliente com a área de trabalho especificada na lista, a informação sobre o cliente será 
 adicionada a uma nova lista. Essa lista será retornada como resultado da execução da função quando ela 
 finalizar sua execução.

Chame a função para a área "Transportation", para fazer um teste. Em seguida, imprima a lista filtrada (
já no pré-código).'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

clients_list = clients

def filter_clients(clients_list,field):
    filtered_list=[]
    for client in clients_list:
        if client[4] == field:
            filtered_list.append(client)
    return filtered_list# crie sua função filter_clients aqui

filtered_list = filter_clients(clients_list,'Transportation')

  # imprimimos o resultado aqui
print(filtered_list)


'''Tarefa 2 - lição prática - cap3 - sprint2

Vamos torná-la ainda mais flexível! Escreva mais duas funções similares à anterior que chamamos:

filter_age() e
filter_income()

Na primeira função, usaremos a idade como o filtro, enquanto na segunda, vamos usar a renda como o filtro.

A lista clients deve ser usada como argumento para o parâmetro clients_list em ambas as funções, de forma 
parecida ao que você fez na tarefa anterior.

Ambas as funções devem filtrar os clientes com valores maiores do que o valor passado como um argumento 
na chamada da função.

Chame a função filter_age() e filtre a lista clients, extraindo os clientes que tenham mais de 40 anos. 
Armazene os resultados na variável filtered_age. 

Da mesma forma, chame a função filter_income() e filtre a lista clients, extraindo apenas os clientes que 
tenham uma renda maior que 250.000. Salve os resultados na variável filtered_income.

Imprima as variáveis filtered_age e filtered_income (que já estão no pré-código).'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# escreva duas funções de filtragem aqui: filter_age e filter_income
def filter_age(clients_list,age):
    filtered_age = []
    for client in clients_list:
        if client[2] > age:
            filtered_age.append(client)
    return filtered_age
    
def filter_income(clients_list,income):
    filtered_income = []
    for client in clients_list:
        if client[3] > income:
            filtered_income.append(client)
    return filtered_income  


filtered_age = filter_age(clients,40)# chame a função filter_age aqui
filtered_income = filter_income(clients,250000) # chame a função filter_income aqui

# imprime o resultado
print(filtered_age)
print(filtered_income)


'''CAPÍTULO 04

LIÇÃO 03

Tarefa 01
Importe pandas de forma que a biblioteca possa ser acessada utilizando pd. Crie uma lista aninhada, 
music, com quatro elementos. Cada sublista deve armazenar dois valores string — artista e nome da música:

'Bob Dylan' — 'Like A Rolling Stone'
'John Lennon' — 'Imagine'
'The Beatles' — 'Hey Jude'
'Nirvana' — 'Smells Like Teen Spirit' '''

import pandas as pd 

music = [
    ['Bob Dylan','Like A Rolling Stone'],
    ['John Lennon','Imagine'],
    ['The Beatles','Hey Jude'],
    ['Nirvana','Smells Like Teen Spirit']
]

print(music)


'''Tarefa 2
Crie uma lista chamada entries com dois elementos: os nomes das colunas 'artist' e 'track'. 
Em seguida, use a classe DataFrame() para criar uma tabela a partir das listas music e entries. 
Armazene o resultado na variável playlist e o imprima.'''

import pandas as pd

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit'],
]

entries = ['artist','track']

playlist = pd.DataFrame(data=music , columns=entries)

print(playlist)



'''LIÇÃO 5'''

'''Tarefa 1
Escreva o código que recupera o nome da música da 8ª linha do conjunto de dados. Os nomes das músicas 
estão localizados na coluna 'track'. Atribua o valor obtido à variável result e imprima-o.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

result = df.loc[7,'track']
print(result)


'''Tarefa 2
Agora vamos praticar a indexação.

Fatie o DataFrame df, extraindo todos os valores para a coluna 'genre' entre a terceira e a décima
primeira linha. 
Armazene os valores extraídos na variável index_res e imprima-os.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

index_res = df.loc[2:10,'genre']# Escreva seu código aqui

print(index_res)


'''Tarefa 3
Divida o DataFrame df, extraindo as células da 6ª linha para as colunas entre 'total play' e 'genre'.
Armazene os valores extraídos na variável index_res e imprima-os.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

index_res = df.loc[5, 'total play': 'genre']

print(index_res)


'''Tarefa 4
É hora de ver como a notação abreviada funciona na prática.

Selecione a coluna 'user_id' do DataFrame df usando a notação abreviada e armazene-a na variável 
index_res. 
Imprima index_res no final.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

index_res = df['user_id']# Escreva seu código aqui

print(index_res)


'''Tarefa 5
Obtenha as colunas 'user_id' e 'track' do DataFrame df usando a notação abreviada e armazene-as na 
variável index_res. 
Imprima index_res no final.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

index_res = df[['user_id','track']]# Escreva seu código aqui

print(index_res)


'''Tarefa 6
Extraia da linha 10 à linha 20 do DataFrame df usando notação abreviada e armazene o 
resultado na variável index_res. 
Imprima index_res no final.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

index_res = df[9:20]# Escreva seu código aqui

print(index_res)



'''LIÇÃO 6'''

'''Tarefa 1
Vamos praticar um pouco agora.

Use a indexação lógica para filtrar o DataFrame armazenado na variável df.
A tabela resultante deve conter apenas linhas com 'genre' igual a 'jazz'. 
Armazene a tabela filtrada na variável jazz_df e imprima-a.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

jazz_df = df.loc[df.loc[:,'genre'] == 'jazz']# Escreva seu código aqui

print(jazz_df)



'''Tarefa 2
Agora vamos usar a indexação lógica para filtrar o DataFrame novamente.
Filtre a tabela original para incluir apenas as músicas com 'total play' superior a 90 segundos.
Armazene a tabela filtrada na variável high_total_play_df e imprima-a.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

high_total_play_df = df.loc[df['total play'] > 90]# Escreva seu código aqui

print(high_total_play_df)



'''LIÇÃO7'''

'''Tarefa 1
Em cenários da vida real, as empresas costumam ter perguntas específicas que exigem respostas.
Por exemplo, uma empresa talvez precise analisar os dados de um usuário específico com o 'user_id' igual 
a '5D9AAD37'.

Vamos fazer isso agora. Para conseguir isso, você precisa filtrar a tabela para extrair apenas as linhas 
relevantes para o usuário ('5D9AAD37'). Em seguida, pediremos que você calcule a duração média das músicas que esse usuário reproduziu. 
Essas informações são armazenadas na coluna 'total play'. 
Após calcular, armazene os resultados na variável user_mean_dur e a imprima.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

user_mean_dur = df[df['user_id'] == '5D9AAD37']['total play'].mean()

print(user_mean_dur)


'''Tarefa 2
Escreva o código para contar o número de músicas para as quais 'Aura' é o artista. 
Você vai precisar da coluna 'Artist' para fazer isso. 
Armazene o resultado na variável aura_count. 
Não se esqueça de imprimir este número.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

aura_count = df[df['Artist'] == 'Aura']['Artist'].count()

print(aura_count)


'''Tarefa 3
Escreva código para calcular o número total de segundos que nossos usuários ouviram as músicas do 
artista 'Zodiac'. 
Armazene o resultado na variável zodiac_total e imprima-o.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

zodiac_total = df[df['Artist'] == 'Zodiac']['total play'].sum()

print(zodiac_total)



'''
LIÇÃO PRÁTICA - CAPÍTULO 4

Crie uma lista de listas intituladas state_animals. Cada lista contém dois valores string: o nome de um 
estado e seu animal correspondente. A lista state_animals deve ter dez elementos.

Em seguida, crie uma lista chamada col_names com dois elementos: os nomes das colunas 'state' e 'animal'.

A etapa final é criar um DataFrame com state_animals como valores e col_names como nomes das colunas. 
Armazene este DataFrame na variável df e imprima-o.

'Alabama' — 'black bear'
'Alaska' — 'moose'
'Arizona' — 'ringtail'
'Arkansas' — 'white-tailed deer'
'California' — 'grizzly bear'
'Colorado' — 'rocky Mt. bighorn sheep'
'Connecticut' — 'sperm whale'
'Delaware' — 'gray fox'
'Florida' — 'manatee'
'Georgia' — 'white-tailed deer'
'''

import pandas as pd

state_animals= [
    ['Alabama','black bear'],
	['Alaska','moose'],
	['Arizona','ringtail'],
	['Arkansas','white-tailed deer'],
	['California','grizzly bear'],
	['Colorado','rocky Mt. bighorn sheep'],
	['Connecticut','sperm whale'],
	['Delaware','gray fox'],
	['Florida','manatee'],
	['Georgia','white-tailed deer']
]

col_names = ['state','animal']# Escreva seu código aqui

df = pd.DataFrame(data=state_animals , columns=col_names)

print(df)


'''Vamos praticar a indexação do DataFrame usando o conjunto de dados music_log_chpt_11.csv que vimos antes. 
Seu objetivo é usar a notação .loc[] para extrair as linhas 2 a 600 para as colunas do DataFrame Artist e 
track. 
Armazene a fatia extraída na variável sliced e imprima-a.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

sliced = df.loc[1:599,['Artist','track']] # Escreva seu código aqui

print(sliced)


'''
CAPÍTULO 05

LIÇÃO 03 - Renomear colunas


Tarefa 1
Agora é sua vez de praticar!

Primeiro, você precisa saber se algo está errado com os nomes das colunas e o que exatamente está errado. 
Então comece imprimindo os nomes das colunas da tabela df.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

print(df.columns)


'''Tarefa 2
Você deve ter identificado três problemas nos nomes das colunas ' user_id', 'total play' e 'Artist'. 
Então vá em frente e corrija-os.

Renomeie as três colunas a seguir em df:

'  user_id' → 'user_id'
'total play' → 'total_play'
'Artist' → 'artist'
Crie um dicionário com os nomes antigos e novos das colunas e então chame o método rename() em df e passe 
seu dicionário para ele.

No dicionário, use os nomes das colunas antigas como chaves e as novas como valores.

Em seguida, imprima o atributo columns de df para confirmar que as alterações foram aplicadas.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')
df_new = pd.read_csv('/datasets/music_log_raw.csv')

columns = [' user_id','total play','Artist']

columns_new = {
    '  user_id':'user_id',
    'total play':'total_play',
    'Artist':'artist'
}

df = df.rename(columns = columns_new) #método rename com reatribuição
print(df.columns)

df_new.rename(columns=columns_new,inplace = True) #método rename sem reatribuição, apenas com a especificação do parâmetro inplace como True.
print(df_new.columns)

'''
Tarefa 3
Agora queremos que você faça a mesma renomeação, mas usando 3 métodos de string: strip(), lower() e 
replace(). Coloque os novos nomes das colunas na lista new_col_names.

Em seguida, imprima o atributo columns de df para confirmar que as alterações foram aplicadas.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

new_col_names = []

for columns in df.columns:
    name_stripped = columns.strip()
    name_lowered = name_stripped.lower()
    name_replaced = name_lowered.replace(' ','_')
    new_col_names.append(name_replaced)
df.columns = new_col_names

print(df.columns)



'''
CAPÍTULO 05

LIÇÃO 04 - Processamento de valores ausentes

Tarefa 1
Escreva um código que some o número de valores ausentes em todas as colunas do conjunto de dados. 
Armazene o resultado na variável mis_val e imprima-o.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

mis_val = df.isna().sum()# Escreva seu código aqui

print(mis_val)


''' 
  Tarefa 2
Escreva código para percorrer as colunas genre, Artist e track do DataFrame df e substitua todos os 
valores ausentes pela string 'no_info'. A lista de colunas a serem substituídas está armazenada na 
variável columns_to_replace.

Após realizar as substituições, verifique novamente o número de valores ausentes usando isna().sum()
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

columns_to_replace = ['genre', 'Artist', 'track']

for col in columns_to_replace:
	df[col].fillna('no_info',inplace=True)# Escreva seu código aqui

print(df.isna().sum())


''' 
Tarefa 3
Agora vamos remover NaNs na coluna total play substituindo-os por 0.

Após realizar as substituições, verifique novamente o número de valores ausentes usando isna().sum()
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

df['total play'].fillna(0,inplace=True)

print(df.isna().sum())



'''
CAPÍTULO 05

LIÇÃO 05 - Processamento de valores duplicados

Tarefa 1
No trecho de código abaixo, você encontrará a variável pop, que armazena um DataFrame filtrado contendo 
apenas músicas pop. Seu objetivo é determinar o número de duplicados neste DataFrame e armazenar este 
valor na variável duplicates. 
E, finalmente, imprima esta variável.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

duplicates = pop.duplicated().sum()# Escreva seu código aqu

print(duplicates)


''' 
Tarefa 2
Usando os dados da tarefa anterior, agora precisamos descartar as linhas duplicadas do DataFrame pop. 
O DataFrame resultante deve ser armazenado na mesma variável pop. Depois de limpar o DataFrame, 
verifique novamente o número de duplicados e imprima esse número.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

pop = pop.drop_duplicates()# Escreva seu código aqui

print(pop.duplicated().sum())


''' 
Tarefa 3
Chegou a hora de verificar o número de valores únicos na coluna 'Artist'. Armazene os valores únicos 
na variável pop_artists. 
O número de artistas únicos deve ser posto na variável n_artists. Imprima ambas as variáveis.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

pop_artists = pop['Artist'].unique()# Escreva seu código aqui
n_artists = pop['Artist'].nunique()# Escreva seu código aqui

print(pop_artists)
print(n_artists)



'''CAPÍTULO 05

LIÇÃO 06 - Agrupamento de dados

Tarefa 1
Vamos dar mais uma olhada no nosso conjunto de dados de música e agrupá-lo de maneira semelhante à que 
fizemos com os exoplanetas. 
É importante observar que o agrupamento é geralmente executado em um conjunto de dados tratado, 
que não possui NaNs, duplicados ou nomes de coluna não formatados. Portanto, não usaremos o conjunto de 
dados music_log_raw.csv original e, em vez disso, usaremos o conjunto de dados pré-processado com todos
 os problemas eliminados.

A primeira etapa é agrupar o conjunto de dados por 'genre'. Quando o agrupamento for aplicado, 
armazene o resultado na variável genre_groups e imprima seu tipo.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre')# Escreva seu código aqui

print(type(genre_groups))


'''Tarefa 2
Agora vamos passar para o ambiente de aplicação e aplicar métodos computacionais a cada grupo. 
Lembre-se de que, eventualmente, queremos calcular o tempo total. Quando queremos encontrar o tempo total,
o método que precisamos aplicar deve nos dar uma soma como resultado. Aplique ao pré-código abaixo o 
método apropriado (quando for adicionada, a variável genre_groups vai armazenar um DataFrame com o resultado). 
Quando terminar, imprima a variável genre_groups.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre').sum() # aplique o método apropriado aqui

print(genre_groups)


''' 
Tarefa 3
Nosso passo final é combinar os resultados. Não se esqueça, queremos calcular o tempo total que nossos 
ouvintes passaram ouvindo cada gênero. Temos uma coluna 'total_play' em nosso conjunto de dados que
 contém exatamente o que precisamos. Precisamos passar isso para o nosso agrupamento: primeiro, selecione 
 a coluna e então aplique um método que calcule o tempo total.

Faça isso e imprima o resultado final.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre')['total_play'].sum()# Escreva seu código aqui

print(genre_groups)



'''CAPÍTULO 05

LIÇÃO 07 - Ordenamento de dados

Tarefa 1
Tarefa 1
Na lição anterior, você agrupou nossos dados music_log_processed.csv por 'genre' e calculou o tempo total
que nossos ouvintes passaram ouvindo cada gênero. 
O resultado para cada 'genre', temos o tempo total ouvido. Ele está armazenado na variável time_by_genre 
no pré-código.

Agora, vamos ordenar os resultados por ordem decrescente e ver os 10 principais gêneros que nossos 
ouvintes mais ouviram. Faça isso e salve os resultados na variável time_by_genre_sort.

Observe que para esta tarefa, você não precisa especificar a coluna pela qual os dados precisam ser 
ordenados, já que há apenas uma coluna na variável time_by_genre.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

time_by_genre = df.groupby('genre')['total_play'].sum()

time_by_genre_sort = time_by_genre.sort_values(ascending=False) # Escreva seu código aqui

print(time_by_genre_sort.head(10))


