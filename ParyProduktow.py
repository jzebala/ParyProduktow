import pandas as pd
from itertools import combinations
from collections import defaultdict

# Wczytaj dane z pliku CSV z uwzględnieniem średnika jako separatora
file_path = 'zamowienia.csv'
df = pd.read_csv(file_path, sep=';')

# Sprawdzenie, czy plik zawiera odpowiednie kolumny
if 'ID ZAMÓWIENIA' not in df.columns or 'SKU' not in df.columns:
    raise ValueError("Plik CSV musi zawierać kolumny 'ID ZAMÓWIENIA' oraz 'SKU'")

# Wybór rozmiaru kombinacji (2 dla par, 3 dla trójek, itd.)
combination_size = 2

if combination_size < 2:
    raise ValueError("Rozmiar kombinacji musi być co najmniej 2.")

# Grupowanie produktów według zamówienia (usnięcie dupliaktów)
orders = df.groupby('ID ZAMÓWIENIA')['SKU'].apply(lambda x: sorted(set(x)))

# Tworzenie listy kombinacji produktów dla każdego zamówienia
combination_orders = defaultdict(list)
for order_id, products in orders.items():
    if len(products) >= combination_size:
        for combination in combinations(sorted(products), combination_size):
            combination_orders[combination].append(order_id)

# Liczenie wystąpień każdej kombinacji
combination_counts = {combination: len(order_ids) for combination, order_ids in combination_orders.items()}

# Przygotowanie danych do zapisania
results = []
for combination, count in combination_counts.items():
    results.append({
        'Kombinacja produktów': combination,
        'Wystąpienia': count,
        'Zamówienia': ', '.join(map(str, combination_orders[combination]))  # Łączenie listy zamówień w jeden ciąg tekstowy
    })

# Tworzenie DataFrame
results_df = pd.DataFrame(results)

# Sortowanie DataFrame według liczby wystąpień (malejąco)
results_df = results_df.sort_values(by='Wystąpienia', ascending=False)

# Zapisanie do pliku CSV
output_file_path = f'wyniki_kombinacji_produktow_{combination_size}.csv'
results_df.to_csv(output_file_path, index=False, sep=';')

print(f"Wyniki zapisano do pliku {output_file_path}")
