"""Napisz funkcję, która wczytuje liczbę od użytkownika i oblicza jej n-tą potęgę,
gdzie n jest również wczytane od użytkownika. 
Obsłuż wyjątki dlanieprawidłowych danych wejściowych oraz niepoprawnych wartości dla liczby iwykładnika."""


def raise_to_power():
    base=int(input("Set the base number you want to raise to power: "))
    power=int(input("Set the power you want to raise the number to: "))
    solution=base**power
    print(solution)
    return solution

raise_to_power()