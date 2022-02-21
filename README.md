# Kartezjana

Funkcja w pythonie zamienia słownik w listę słowników zawierające wszelkie możliwe kombinacje


Zasada działania : 
W pętli wczytuje się ilość ilości cech potrzebnych do obliczenia kombinacji : 

Możliwość kombinacji jest równa iloczynowi : Np :

Wysokość  20, 40 [cm]
szerokość 100, 30, 20 cm

Ilość kombimacji : 2*3 = 6

20 100
20 30
20 20
40 100
40 30
40 20

Następnie ponieważ zadanie wymaga aby działało dla dowolnej długości : 
Tworzona jest lista liczników dla każdej z cech 
Liczniki będą działać metodą inkrementacji łańcuchowej 

Przykład 
Maksymalne wartości dla danej cechy: 

[3,2,4]
1 iteracja 
[0,0,0]
[0,0,1]
[0,0.2]
[0,0,4]
[0,1,0]
itd.. 
w ten sposób można wykonać zadanie bez zagnieżdżonej pętli for, którą w zasadzie trudno użyć, ponieważ wymaga
znajomości ilości cech, a tej wiadomości nie znamy 


