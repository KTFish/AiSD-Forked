# Zmodyfikować kod z zadania poprzedniego w taki sposób, aby komunikaty wyświetlane na ekranie utworzyć metodą interpolacji stringów

first_name = 'Grzegorz'
last_name = 'Brzeczeszczykiewicz'
balance = 20000.5

name = f'{first_name} {last_name}'

message = f'Witaj, {name}. Twój stan konta to {balance} PLN w zmiennej message.'

print(message)
