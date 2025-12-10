from text_analyzer import leggi_file, conta_caratteri, frequenza_caratteri

def run_analysis():
    print("__ Analizzatore di testo__")

    file_path = input("Inserisci il percorso del file di testo (es: prova.txt): ")

    try:
        # 2. Utilizzo delle Funzioni Importate
        
        # Legge il contenuto del file (gestisce gli errori di I/O)
        contenuto_file = leggi_file(file_path)
        
        # Calcola il totale dei caratteri
        totale_caratteri = conta_caratteri(contenuto_file)
        
        # Calcola la frequenza di tutti i caratteri
        frequenze = frequenza_caratteri(contenuto_file)
        
        # 3. Output 1: Totale Caratteri
        print("\n" + "="*40)
        print("Risultati dell'Analisi")
        print("="*40)
        print(f"**Numero totale di caratteri:** {totale_caratteri}")
        
        # 4. Output 2: Caratteri con Frequenza > 5
        print("\n**Caratteri che compaiono più di 5 volte:**")
        
        # Filtra il dizionario: crea un nuovo dizionario solo con i conteggi > 5
        caratteri_frequenti = {
            char: count 
            for char, count in frequenze.items() 
            if count > 5
        }
        
        if caratteri_frequenti:
            # Ordiniamo per frequenza decrescente (opzionale, ma migliora la leggibilità)
            risultati_ordinati = sorted(caratteri_frequenti.items(), key=lambda item: item[1], reverse=True)
            for char, count in risultati_ordinati:
                # Gestiamo la stampa dello spazio per chiarezza
                display_char = f"'{char}'" if char != ' ' else "[spazio]"
                print(f"- {display_char.ljust(10)}: {count} volte")
        else:
            print("Nessun carattere compare più di 5 volte nel testo analizzato.")

        print("="*40)

    except FileNotFoundError as e:
        # Cattura l'errore sollevato da leggi_file()
        print(f"\n**ERRORE:** {e}")
    except Exception as e:
        # Cattura qualsiasi altro errore imprevisto
        print(f"\n**ERRORE IMPREVISTO:** {e}")

if __name__ == "__main__":
    run_analysis()