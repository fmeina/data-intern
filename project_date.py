import csv

with open('dane.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile, delimiter=';'))


class DataAnalize:

    def Average(self):
        sex = input("Wybierz płeć dla której sprawdzasz statystyki(wpisz k/m, aby sprawdzić obie płci wciśnij enter i przejdź dalej): ")
        voivodeship = input("Wybierz wojewodztwo(pamiętaj żeby zacząć z wielkiej litery): ")
        year = input("Podaj rok: ")
        i = 0
        avg = []
        if sex == 'k':       
            for i in range(len(data)):
                if data[i][0] == voivodeship:
                    if data[i][1] == 'przystąpiło':
                        if data[i][2] == 'kobiety':
                            if data[i][3] == year:
                                avg.append(data[i][4])
                            
                i+=1
                years = int(year)
                years -=1
                year = str(years)

            j = 0
            for j in range(len(avg)):
                average = avg[j] / len(avg)
            print("Średnia liczba osób przystępujących do matury to: ", average)
            return average
        
        elif sex == 'm':
            for i in range(len(data)):
                if data[i][0] == voivodeship:
                    if data[i][1] == 'przystąpiło':
                        if data[i][2] == 'mężczyźni':
                            if data[i][3] == year:
                                avg.append(data[i][4])
                            
                i+=1
                years = int(year)
                years -=1
                year = str(years)
            j = 0
            for j in range(len(avg)):
                average = avg[j] / len(avg)
            print("Średnia liczba osób przystępujących do matury to: ", average)
            return average
        else:
            both = 0
            for i in range(len(data)):
                if data[i][0] == voivodeship:
                    if data[i][1] == 'przystąpiło':
                        if data[i][3] == year:
                            both = int(data[i][4]) + int(data[i+1][4])
                            avg.append(both)
                            
                i+=1
                years = int(year)
                years -=1
                year = str(years)
            j = 0
            for j in range(len(avg)):
                average = avg[j] / len(avg)
            print("Średnia liczba osób przystępujących do matury to: ", average)
            return average

    def Percentage(self):
        sex = input("Wybierz płeć dla której sprawdzasz statystyki(wpisz k/m, aby sprawdzić obie płci wciśnij enter i przejdź dalej): ")
        voivodeship = input("Wybierz wojewodztwo(pamiętaj żeby zacząć z wielkiej litery): ")
        attend = []
        passed = []
        if sex == 'k':
            for i in range(len(data)):
                if data [i][0] == voivodeship:
                    if data [i][2] == 'kobiety':
                        if data[i][1] == 'przystąpiło':
                            attend.append(data[i][4])
                        if data[i][1] == 'zdało':
                            passed.append(data[i][4])
                percent = (passed[i]/attend[i]) * 100
                print("W roku ",data[i][3], " maturę zdało", percent, " % ludzi" )

        elif sex == 'm':
            for i in range(len(data)):
                if data [i][0] == voivodeship:
                    if data [i][2] == 'mężczyźni':
                        if data[i][1] == 'przystąpiło':
                            attend = data[i][4]
                        if data[i][1] == 'zdało':
                            passed = data[i][4]
                        percent = (float(passed[i])/float(attend[i])) * 100
                        print("W roku ",data[i][3], " maturę zdało", percent, " % ludzi" )

        else:
            for i in range(len(data)):
                if data [i][0] == voivodeship:
                    if data[i][1] == 'przystąpiło':
                        attend = int(data[i][4]) + int(data[i+1][4])                   
                    if data[i][1] == 'zdało':
                        passed = int(data[i][4]) + int(data[i+1][4])
                    percent = (passed[i]/attend[i]) * 100
                    print("W roku ",data[i][3], " maturę zdało", percent, " % ludzi" )

    def Best(self):
        sex = input("Wybierz płeć dla której sprawdzasz statystyki(wpisz k/m, aby sprawdzić obie płci wciśnij enter i przejdź dalej): ")
        year = input("Podaj rok dla którego chcesz sprawdzić najlepsze wodewództwo: ")
        i = 0
        better = 0
        if sex == 'k':
            for i in range(len(data)-1):
                if data[i][2] == 'kobiety':  
                    if data[i][3] == year:
                        if data[i][1] == 'zdało':
                            if int(data[i][4]) > int(data[i+1][4]):
                                better = data[i][0]
                            else:
                                better = data[i+1][0]

            print("Najlepsze zdawalność w podanym roku była w województwie: ", better)

        elif sex == 'm':
            for i in range(len(data)-1):
                if data[i][2] == 'mężczyźni':  
                    if data[i][3] == year:
                        if data[i][1] == 'zdało':
                            if int(data[i][4]) > int(data[i+1][4]):
                                better = data[i][0]
                            else:
                                better = data[i+1][0]

            print("Najlepsze zdawalność w podanym roku była w województwie: ", better)
        else:
           for i in range(len(data)-1):
                    if data[i][3] == year:
                        if data[i][1] == 'zdało':
                            passed1 = int(data[i][4]) + int(data[i+1][4])
                            passed2 =int(data[i+2][4]) + int(data[i+3][4])
                            if passed1 > passed2 :
                                better = data[i][0]
                            else:
                                better = data[i+1][0]

           print("Najlepsze zdawalność w podanym roku była w województwie: ", better)

    def Regres(self):
        sex = input("Wybierz płeć dla której sprawdzasz statystyki(wpisz k/m, aby sprawdzić obie płci wciśnij enter i przejdź dalej): ")
        if sex == 'k':
            for i in range(len(data)-1):
                if data [i][2] == 'kobiety': 
                    if data[i][1] == 'zdało':
                        if data[i][4] > data[i-1][4]:
                            print("Województwo ", data[i][0], " : ", data[i][3], " -> ", data[i+1][3])
                        else:
                            continue

        elif sex == 'm':
            for i in range(len(data)-1):
                if data [i][2] == 'mężczyźni': 
                    if data[i][1] == 'zdało':
                        if data[i][4] > data[i-1][4]:
                            print("Województwo ", data[i][0], " : ", data[i][3], " -> ", data[i+1][3])
                        else:
                            continue
        else:
            for i in range(len(data)-1):
                if data[i][1] == 'zdało':
                    passed1 = int(data[i][4]) + int(data[i+1][4])
                    passed2 =int(data[i+2][4]) + int(data[i+3][4])
                    if passed1 > passed2 :
                        print("Województwo ", data[i][0], " : ", data[i][3], " -> ", data[i+1][3])
                    else:
                        continue

    def Compare(self):
        sex = input("Wybierz płeć dla której sprawdzasz statystyki(wpisz k/m, aby sprawdzić obie płci wciśnij enter i przejdź dalej): ")
        voivodeship1 = input("Podaj pierwsze województwo do porównania: ")
        voivodeship2 = input("Podaj drugie województwo do porównania: ")
        i = 0
        wynik1 = 0
        wynik2 = 0
        for i in range(len(data)):
            if sex == 'k':
                 if data[i][2] == 'kobiety':  
                     if data[i][1] == 'zdało':
                        if data[i][0] == voivodeship1:
                            wynik1 = int(data[i][4])
                        if data[i][0] == voivodeship2:
                            wynik2 = int(data[i][4])
                        if wynik1 > wynik2:
                            print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship1)
                        else:
                            print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship2)
            elif sex == 'm':
                if data[i][2] == 'mężczyźni':  
                    if data[i][1] == 'zdało':
                        if data[i][0] == voivodeship1:
                            wynik1 = int(data[i][4])
                        if data[i][0] == voivodeship2:
                            wynik2 = int(data[i][4])
                        if wynik1 > wynik2:
                            print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship1)
                        else:
                            print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship2)
            else:
                if data[i][1] == 'zdało':
                    if data[i][0] == voivodeship1:
                        wynik1 = int(data[i][4]) + int(data[i+1][4])
                    if data[i][0] == voivodeship2:
                        wynik2 = int(data[i][4]) + int(data[i+1][4])
                    if wynik1 > wynik2:
                        print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship1)
                    else:
                        print("Lepszą zdawalność w roku ", data[i][3],"miało województwo ", voivodeship2)




menu = '''
Wybierz opcję:
1 - obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie
2 - obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat
3 - podanie województwa o najlepszej zdawalności w konkretnym roku
4 - wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze
5 - porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku
---------------
aby zatrzymać skrypt wybierz opcję 0
'''    

analyze = DataAnalize()

while True:
    print(menu)
    letter =int(input())
    if letter == 1:
       analyze.Average()
       print("\nAby kontynuować wciśnij ENTER...\n")
       input()
       continue
    elif letter == 2:
        analyze.Percentage()
        print("\nAby kontynuować wciśnij ENTER...\n")
        input()
        continue
    elif letter == 3:
        analyze.Best()
        print("\nAby kontynuować wciśnij ENTER...\n")
        input()
        continue
    elif letter == 4:
        analyze.Regres()
        print("\nAby kontynuować wciśnij ENTER...\n")
        input()
        continue
    elif letter == 5:
        analyze.Compare()
        print("\nAby kontynuować wciśnij ENTER...\n")
        input()
        continue
    elif letter == 0:
        break
    else:
        print("Musisz wybrać prawidłową opcję. Wciśnij ENTER i spróbuj ponownie...")
        input()
        continue