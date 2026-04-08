wzrost = float(input('Podaj wzrost: '))
opiekun = input('Czy jest opiekun: ')
if wzrost < 120:
    print('Nie wchodzisz!')
elif (120 <= wzrost < 160 and opiekun == 'tak') or (wzrost >= 160):
    print('Wchodzisz.')
else:
    print('Nie Wchodzisz')
