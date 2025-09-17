#elif combinado com for

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