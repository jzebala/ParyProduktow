# ParyProduktow
Skrypt wczytuje plik CSV z zamówieniami oraz produktami przypisanymi do zamówienia, a następnie wyznacza najczęściej występujące pary produktów.
## A na co to komu?
Prowadząc sprzedaż, warto wiedzieć, które kombinacje produktów sprzedają się najczęściej. Takie dane pozwalają zaplanować dobrą kampanię marketingową lub utworzyć zestaw produktów (który może sprzedawać się lepiej niż pojedyncze produkty).
Również takich danych można użyć do proponowania klientowi komplementarnych produktów do tych już znajdujących się w koszyku zakupowym.
## Jak używać?
Plik CSV __zamówienia.csv__ z danymi powinien zawierać dwie kolumny __ID ZAMÓWIENIA__ oraz __SKU__.
Domyślnie skrypt wyszukuję najczęściej występujące pary produktów w zamówieniach. Jednak tę wartość można zmienić na dowolną, odpowiada za to zmienna _combination_size_.
```
combination_size = 2
```
Przykładowo zmieniając wartość tej zmiennej na 3, skrypt wyznaczy kombinację trzech najczęściej występujący produktów w zamówieniach.
## Rezultat
Wynik działania skryptu zapisywany jest do pliku CSV. Plik z wynikami zawiera trzy kolumny:
1. __Kombinacja produktów__ - Kombinacja produktów (pary, trójki lub więcej)
2. __Wystąpienia__ - Ilość wystąpień danej kombinacji produktów
3. __Zamówienia__ - Numer zamówienia, w którym wystąpiła kombinacja
