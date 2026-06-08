
# Utworzenie krotki (tuple)
punkt = (10, 20, 30)
print(punkt)
punkt[0] = 15
print(punkt)

# punkt[0] = 15
# Próba zmiany elementu krotki powoduje błąd:

# TypeError: 'tuple' object does not support item assignment

# Krotki w Pythonie są niemutowalne (immutable) czyli po utworzeniu nie można
# zmieniać ich modyfikować
