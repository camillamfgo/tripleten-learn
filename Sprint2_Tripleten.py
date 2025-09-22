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