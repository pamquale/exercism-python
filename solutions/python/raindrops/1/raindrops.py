def convert(number):
    pling = ''
    plang = ''
    plong = ''
    if number % 3 == 0:
        pling = 'Pling'
    if number % 5 == 0:
        plang = 'Plang'
    if number % 7 == 0:
        plong = 'Plong'
    if number % 3 != 0 and number % 5 !=0 and number % 7 != 0:
        return f'{number}'
    return pling + plang + plong
