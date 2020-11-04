# Utworzyć zmienne:
# first_name, do której zostanie podstawione imie
# last_name, do której zostanie podstawione nazwisko
# balance, do której zostanie podstawiony stan konta
# name, w której znajdzie się pełne imię i nazwisko pochodzące ze zmiennych first_name i last_name
# message, w której znajdzie się treść komunikatu o następującej formie: ""
# Następnie należy wyswietlić na ekranie ekranie treść komunikatu zajdującego sięWitaj, [name]. Twój stan konta to [balance] PLN w zmiennej message.

first_name = 'Grzegorz'
last_name = 'Brzeczeszczykiewicz'
balance = 20000.5

name = first_name + ' ' + last_name

message = 'Witaj, ' + name + '. Twój stan konta to ' + str(balance) + ' PLN'

print(message)
