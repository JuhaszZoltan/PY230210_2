file = open(file='nevek.csv', mode='a', encoding='utf-8')

print('a bekérés befejezéséhez hagyja a "név" mezőt üresen!')

while True:
    nev:str = input('írd be a nevet: ')
    if nev == '': break
    avg:float = float(input(f'írd be {nev} tanulmányi átlagát: '))
    file.write(f'{nev};{avg}\n')
print('vége!')