""" Napisz program, który wczytuje dane od użytkownika w formacie klucz:wartość i zapisuje je do słownika.
 Obsłuż wyjątki dla nieprawidłowych danych wejściowych oraz prób dodania już istniejącego klucza do słownika."""



StartDict={}
while True:
    data=str(input("Wprowadź dane w formacie klucz:wartość : "))
    if(":" not in data):
        print("Nieprawidłowe dane wejściowe - wpisz je według klucza. Pamiętaj użyj ':' a nie ';'. ")
    elif(data[0]==":"):
        print("Nieprawidłowe dane wejściowe: znak ':' nie może być pierwszy")
    elif(data[-1]==":"):
        print("Nieprawidłowe dane wejściowe znak ':' nie może być ostatni")
    else:
        listedData=data.split(":")
        key=listedData[0]
        val=listedData[1]
        if (key not in StartDict and val not in StartDict):
            StartDict.update({key:val})
            print(f"Dane zostały wprowadzone, słownik to: {StartDict}")
        else:
            print("Wprowadzone dane są już obecne w słowniku")
        

