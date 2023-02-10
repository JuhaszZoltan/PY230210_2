file = open(file='diakok.txt', mode='r', encoding='utf-8')

maxmag:int = -1
nev:str = ''

for sor in file:
    d:list[str] = sor.split(' ')
    if maxmag < int(d[2]):
        maxmag = int(d[2])
        nev = f'{d[0]} {d[1]}'

print(f'a legmagasabb diak: {nev} ({maxmag} cm)')