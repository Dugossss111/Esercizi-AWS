import os
import json
from datetime import datetime
import uuid

def aggiungi_corso(corsi_disponibili):
    print("Corsi attuali:", corsi_disponibili)
    nuovo_corso = input("Inserire il nome del nuovo corso:\n").strip()
    if nuovo_corso and nuovo_corso not in corsi_disponibili:
        corsi_disponibili.append(nuovo_corso)
        print(f"Corso '{nuovo_corso}' creato con successo!")
    else:
        print("Nome corso non valido o già esistente.")
    return corsi_disponibili

def iscrivi_partecipante(corsi_disponibili, partecipanti_list, corsi_dict):
    nuovo_partecipante = input("Inserire Nome e Cognome del nuovo partecipante:\n").strip()
    if nuovo_partecipante and nuovo_partecipante not in partecipanti_list:
        partecipanti_list.append(nuovo_partecipante)
    
    corso_scelto = input(f"Inserire il corso a cui iscrivere {nuovo_partecipante}:\n").strip()
    if corso_scelto in corsi_disponibili:
        corsi_dict.setdefault(corso_scelto, {})[nuovo_partecipante] = (0, "")
        print(f"{nuovo_partecipante} iscritto al corso '{corso_scelto}' con successo!")
    else:
        print("Il corso inserito non esiste.")
    
    return partecipanti_list, corsi_dict

def assegna_punteggio(corsi_dict):
    partecipante = input("Nome del partecipante da valutare:\n").strip()
    corso = input("Nome del corso:\n").strip()
    try:
        punteggio = int(input("Numero di Goleador da assegnare (1-10):\n"))
    except ValueError:
        print("Valore non valido!")
        return corsi_dict

    if corso in corsi_dict and partecipante in corsi_dict[corso]:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        corsi_dict[corso][partecipante] = (punteggio, timestamp)
        print(f"Assegnati {punteggio} Goleador a {partecipante} nel corso {corso}.")
    else:
        print("Corso o partecipante non trovato.")
    
    return corsi_dict

def salva_dati_json(corsi_disponibili, partecipanti_list, corsi_dict, file_json):
    dati = {
        "corsi": corsi_disponibili,
        "partecipanti": partecipanti_list,
        "punteggi": corsi_dict
    }
    with open(file_json, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=2, ensure_ascii=False)

def carica_dati_json(file_json):
    if os.path.exists(file_json):
        with open(file_json, "r", encoding="utf-8") as f:
            dati = json.load(f)
            return dati.get("corsi", []), dati.get("partecipanti", []), dati.get("punteggi", {})
    else:
        return [], [], {}

def visualizza_statistiche(corsi_dict):
    print("\n--- Totale Goleador per corso ---")
    for corso, studenti in corsi_dict.items():
        totale = sum(v[0] for v in studenti.values())
        print(f"{corso}: {totale} Goleador")

    punteggi_studenti = {}
    for corso, studenti in corsi_dict.items():
        for studente, (voto, _) in studenti.items():
            punteggi_studenti[studente] = punteggi_studenti.get(studente, 0) + voto
    
    if punteggi_studenti:
        top_student = max(punteggi_studenti, key=punteggi_studenti.get)
        print(f"Top Scorer: {top_student} con {punteggi_studenti[top_student]} Goleador")
    else:
        print("Nessun Goleador assegnato ancora.")

def main():
    file_json = "GoleadorAcademy.json"
    corsi_disponibili, partecipanti_list, corsi_dict = carica_dati_json(file_json)

    print("Benvenuto nel Goleador Academy")
    
    while True:
        print("\n--- MENU ---")
        print("1. Aggiungere un nuovo corso")
        print("2. Aggiungere un nuovo partecipante")
        print("3. Assegna un punteggio a un partecipante")
        print("4. Visualizza statistiche")
        print("0. Esci")
        scelta = input("Scegliere l'azione desiderata:\n").strip()

        if scelta == "1":
            corsi_disponibili = aggiungi_corso(corsi_disponibili)
        elif scelta == "2":
            partecipanti_list, corsi_dict = iscrivi_partecipante(corsi_disponibili, partecipanti_list, corsi_dict)
        elif scelta == "3":
            corsi_dict = assegna_punteggio(corsi_dict)
        elif scelta == "4":
            visualizza_statistiche(corsi_dict)
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida!")

        salva_dati_json(corsi_disponibili, partecipanti_list, corsi_dict, file_json)

if __name__ == "__main__":
    main()