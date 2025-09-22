#elif combinado com for (Tarefa criada por mim)

years = [1975,1982,1992,2005,1972,1985,1998,2010]

for year in years:
    if 1970 <= year < 1980:
        print(f'Nascimento nos anos 70: {year}')
    elif 1980 <= year < 1990:
        print(f'Nascimento nos anos 80: {year}')
    elif 1990 <= year < 2000:
        print (f'Nascimento nos anos 90: {year}')
    else:
        print(f'Não aplicável: {year}')

'''Tarefa 1 - Tripleten
No pré-código, você tem uma lista countries que armazena os países onde determinados filmes foram lançados. Escreva um ciclo for que vai iterar sobre elementos de countries e, para cada elemento, imprimir a mensagem relevante:

Para os USA, vamos imprimir 'The movie was released in the USA.'
Para a França: 'Le film est sorti en France.'
Para a Itália: 'Il film e stato rilasciato in Italia.'
Para qualquer outro país: 'País não definido.' '''

countries = ['France', 'Italy', 'New Zealand', 'Italy', 'France', 'USA']

for country in countries:
    if country == 'USA':
        print('The movie was released in the USA.')
    elif country == 'France':
        print('Le film est sorti en France.')
    elif country == 'Italy':
        print('Il film e stato rilasciato in Italia.')
    else:
        print('País não definido.')       

'''Tarefa 2
As classificações de filmes são armazenadas na variável ratings. Queremos que você converta essas classificações de um sistema de 100 pontos para um sistema de 5 pontos. Para fazer isso, itere sobre a lista ratings original e use instruções condicionais para converter a escala original para o sistema de 5 pontos de acordo com esta lógica:

imprimir 2 se a classificação original estiver na faixa de 0 a 59 pontos, incluindo o último valor
imprimir 3 se a classificação estiver na faixa de 60 a 72 pontos, incluindo o último valor
imprimir 4 se a classificação for de 73 a 84 pontos, incluindo o último valor
imprimir 5 se a classificação for de 85 a 100 pontos, incluindo o último valor'''

ratings = [91, 35, 65, 89, 78, 93]

for rates in ratings:
    if 0 <= rates <= 59:
        print(2)
    elif 60 <= rates <= 72:
        print(3)
    elif 73 <= rates <= 84:
        print(4)
    elif 85 <= rates <= 100:
        print(5)
    else:
         print('Não aplicável')



'''Tarefa
Obtenha todos os filmes dos EUA da tabela movies_info usando um filtro. 
Armazene o resultado na lista movies_filtered. 
Imprima essa lista quando terminar.'''

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

movies_filtered = []

for movie in movies_info:
    if movie[1] == 'USA':
        movies_filtered.append(movie)

print(movies_filtered)


'''Tarefa
Parece que você está se tornando um especialista em filtragem de filmes! 
Continue explorando e filtrando filmes para encontrar seus favoritos.

Agora tente por conta própria:

Crie a lista vazia chamada movies_filtered. 
Em seguida, adicione a movies_filtered filmes que foram lançados em 1994 ou possui uma classificação inferior a 8,5.'''

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

movies_filtered = []# crie uma lista vazia chamada movies_filtered

for movie in movies_info:
    if movie[2] == 1994 or movie[5] < 8.5:
        movies_filtered.append(movie)

for movie in movies_filtered:
    print(movie) 


'''Tarefa 1
O Banco ABC criou uma nova Conta Elite feita sob medida para clientes de alto rendimento líquido que ganham mais de $200.000 anualmente. 
Escreva um código que itere sobre os clientes, verifique se a receita anual de cada
um excede US$ 200.000 e adicione os clientes qualificados à sublista elite_clients, 
que representa a lista de clientes ricos. Por fim, imprima a variável elite_clients.'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

elite_clients = [] # adicione clientes elite aqui
parametro = 200000

for client in clients:
    if client[3] > parametro:
        elite_clients.append(client)
        
print(elite_clients)


'''Tarefa 2
O departamento de marketing quer uma lista de todos os clientes do banco, 
divididos em quatro segmentos de contas. Eles pediram que você crie essa lista. 
Divida todos os clientes do Banco ABC em quatro segmentos: conta Standard para 
clientes com receita inferior a $100.000 (excluindo esse número), conta Plus para 
receitas de US$ 100.000 (incluindo esse número) a US$ 200.000 (excluindo esse número),
conta Elite para receitas de US$ 200.000 (incluindo esse número) a US$ 300.000 
(excluindo esse número) e conta Executive para receitas de US$ 300.000 
(incluindo esse número) ou mais.

No pré-código abaixo, você vai encontrar quatro variáveis com as listas: standard, 
plus, elite e executive. Escreva o código para iterar sobre os clientes, verifique em 
qual categoria a receita se enquadra e adicione-os a uma lista apropriada. 
Quando terminar, imprima a lista de clientes Executive.'''

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

# listas vazias para adicionar clientes
standard = []
plus = []
elite = []
executive = []

for client in clients:
    if client[3] < 100000:
        standard.append(client)
    elif 100000 <= client[3] < 200000:
        plus.append(client)
    elif 200000 <= client[3] < 300000:
        elite.append(client)
    else:
        executive.append(client)


print(executive)



'''Tarefa 3
É o Dia da Juventude, e a equipe de marketing deseja enviar um e-mail direcionado aos 
nossos clientes jovens.

Para melhorar a solução anterior, precisamos atualizar os critérios de idade para 
identificação de clientes jovens.

Atualizamos o código anterior com as novas categorias de jovens.
No entanto, será necessário adicionar os filtros de idade ao filtro anterior de renda 
para que tudo funcione como esperado.

As regras são as seguintes:

standard_young:
Renda anual inferior a $ 100.000 (excluindo esse número) E idade inferior a 40 anos
(excluindo esse número).

plus_young:
Renda anual de $ 100.000 (incluindo esse número) a $ 200.000 (excluindo esse número) 
E idade inferior a 35 anos (excluindo esse número).

elite_young:
Renda anual de $ 200.000 (incluindo esse número) a $ 300.000 (excluindo esse número)
E idade inferior a 35 anos (excluindo esse número).

executive_young:
Renda anual a partir de $ 300.000 (incluindo esse número) E idade inferior a 35 anos 
(excluindo esse número).

Forneça listas atualizadas com base nessas regras e reimprima apenas a lista de 
clientes executive_young.

O comentário no pré-código abaixo vai guiar você nas alterações necessárias. 
Preste atenção nele. Se tiver dificuldades, confira a dica que preparamos.'''

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

standard_young = []
plus_young = []
elite_young = []
executive_young = []

for client in clients:
    if client[3] < 100000 and client[2] < 40:
        standard_young.append(client)
    elif client[3] < 200000 and client[2] < 35:
        plus_young.append(client)
    elif client[3] < 300000 and client[2] < 35:
        elite_young.append(client)
    elif client[3] >= 300000 and client[2] < 35:
        executive_young .append(client)

print(executive_young)


for user in users:
    name = ''
    for purchase_category in user[3]:
        if purchase_category == 'clothes':
            print(f'Nome {user[1][0]} {user[1][1]} que tem {user[2]} anos') #escreva seu código aqui