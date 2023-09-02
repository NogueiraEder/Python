times=( 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense',
        'Athletico-PR', 'Flamengo',
        'internacional', 'Bragantino', 'São Paulo', 'Santo',
        'Botafogo', 'Ceará SC', 'Goiáis', 'Avaí', 'Cuibá',
        'Coritiba', 'Améria-MG', 'Atlético-GO', 'Fortaleza',
        'Juventude')
print(f'os 5 primeiros colocados foram:\n{times[0:5]}')
print(f'os 4 ultimos colocados foram:\n{times[-4:]}')
print(sorted(times))
print(f'o time São Paulo  ficou  {times.index("São Paulo")+1}ª colocaçao')