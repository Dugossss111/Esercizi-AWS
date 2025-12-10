import os
from collections import Counter

def conta_caratteri(testo: str) -> int:
# restituisce il num totale di caratteri nella stringa (spazi inclusi)
    return len(testo)

def frequenza_caratteri(testo: str) -> dict[str, int]:
# restituisce un dict con la frequenza di ogni carattere nel testo    
    return dict(Counter(testo))

def leggi_file(percorso: str) -> str:
# legge il contenuto del file e gestisce l'errore se il file non esiste
    try: 
        with open(percorso, 'r', encoding= 'utf-8') as f:
            contenuto = f.read()
            return contenuto
    except FileNotFoundError:
        # Quando un errore specifico si verifica
        raise FileNotFoundError(f"Errore: File non trovato al percorso specificato: '{percorso}'")
    except Exception as e:
        # Per catturare qualsiasi altro errore di I/O
        raise IOError(f"Si è verificato un errore durante la lettura del file: {e}")    

if __name__ == "__main__":     
    print("Esercizio corretto")