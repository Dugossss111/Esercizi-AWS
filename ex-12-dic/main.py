from requests import post

URL = "https://fakestoreapi.com/products"

while True:
    title = input("Inserisci il titolo del prodotto:"). strip() #toglie gli spazi
    if title:
        break
    print("Il titolo non può essere vuoto!")

while True:
    try:
        price = float(input("Inserisci il prezzo del prodotto:"))
        if price > 0:
            break
        else:
            print("Il prezzo deve essere maggiore di 0")
    except ValueError:
        print("Inserisci un numero valido per il prezzo")
    
while True:
    description = input("Inserisci la descrizione del prodotto:").strip()
    if description:
        break
    print("La descrizione non può essere vuota")

product = {
    "title": title,
    "price": price,
    "description": description,
    "category": "electronics",   # valore fisso
    "image": "https://i.pravatar.cc"  # valore fisso
}

try:
    response = post(URL, json=product)
    response.raise_for_status()
except Exception as e:
    print("Errore nell'invio del prodoto:", e)
else:
    print("Prodotto inviato con successo")
    print(response.json())
    