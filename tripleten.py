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