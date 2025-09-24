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
A função deve retornar uma lista de listas que contenham apenas os filmes lançados após year='''.

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