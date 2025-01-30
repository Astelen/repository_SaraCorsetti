
#Es. funzioni
# Programma che indovina le funzioni
# Funzione che genera numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare il numero generato.

def gioco_numero (numero_utente):
    print("Benvenuto in questo gioco! Il gioco consiste nell'indovinare un numero. Sei pronto?")
    print("Ricorda che puoi sempre uscire dal gioco digitando Esc")
    print("Scrivi il tuo numero: ")
    numero_casuale = numero_utente*2
    if numero_casuale > 100:
        numero_casuale == 100
    while numero_casuale != numero_utente: #ciclo while per permettere all'utente di continuare a giocare
        if numero_utente > numero_casuale:
            print("Il numero da indovinare e' piu' basso! Prova ancora: ")
        elif numero_utente < numero_casuale:
            print("Il numero da indovinare e' piu' alto! Prova ancora: ")
        elif numero_utente == numero_casuale:
            scelta_giocatore = input("Hai indovinato! Vuoi continuare a giocare? Scegli S o N: ")
            if scelta_giocatore.lower() == "s":
                print("Continua a giocare!")
            else:
                print("Ok, alla prossima!")
        elif numero_utente.lower() == "Esc":
            print("Arrivederci!")
            break
        else:
            print("Il numero scelto non e' un numero, devi inserire un numero per giocare. ")

gioco_numero(5)