# Przygotować skrypt, który pobierze od użytkownika (z klawiatury) następujące informacje:
# imie
# rok urodzenia
# i wypisze na ekranie komunikat o następującej formie: "Witaj, [imie]. Masz [x] lat."

first_name = input('Podaj swoje imie: ')
birth_yr = int(input('Podaj swoj rok urodzenia: '))

age = 2020 - birth_yr

print(f'Witaj, {first_name}. Masz {age} lat.')
