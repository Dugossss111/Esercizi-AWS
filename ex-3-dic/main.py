#=====================
#=== Esercizio 1
#=====================

server_list: list[str] = ["web01","db01","cache01"] #definisci la lista

server_list.append("backup01")   #aggiungi elemento
server_list.insert(0, "proxy01") #inserisci un elemento in prima posizione
server_list.remove("cache01")    #rimuovi un elemento

print(server_list) #stampa la lista
print(len(server_list)) #stampa il num di elementi

#=====================
#=== Esercizio 3
#=====================

price_list_u: list[float] = [45.5,12.0, 78.3, 23.1, 56.7]

price_list_o: list[float] = sorted(price_list_u) #ordina la lista e la salva in una nuova lista

print(price_list_o)

print(min(price_list_o))
print(max(price_list_o))

print(23.1 in price_list_o)

counter = 0 
for x in price_list_o:
    if x > 50:
        counter += 1

print(counter)


