
def oblicz_bmi(waga, wzrost):
 return waga/ (wzrost * wzrost)


def opis_bmi(bmi):
 if bmi < 16:
  print('Wygłodzenie')
 elif 16 <= bmi < 17:
  print ('Wychudzenie')
 elif 17 <= bmi < 18.5:
  print('Niedowaga')
 elif 18.5 <= bmi < 25:
  print('Wartość prawidłowa')
 elif 25 <= bmi < 30:
  print('Nadwaga')
 elif 30 <= bmi < 35:
  print('I stopień otyłości')
 elif 35 <= bmi < 40:
  print('II stopień otyłości')
 else:
  print('Otyłość skrajna')

waga = float(input('Ile ważysz?(kg): '))
wzrost = float(input('Ile masz wzrostu?(np. 1.50m): '))


bmi = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI wynosi: {bmi}")
print(f"{opis_bmi(bmi)}")




