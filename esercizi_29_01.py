# Es. 1 if
# prendi imput, capire se e' pari o dispari, stampare

numero_pari = int(input("Ciao! Scrivi un numero e ti diro' se e' pari o dispari: "))

if numero_pari%2 == 0:
     print("Il numero che hai digitato e' pari!")
elif numero_pari%2 != 0:
     print("Il numero che hai digitato e' pari!")
else: print("Questo non e' un numero!")



# Es. 2 while + range
# prende input numero N positivo 

lista_es2 = []
max_lista_es2 = 0
controllore = True

while controllore:
    numero_es2 = int(input("Scrivi un numero intero positivo: "))
    for numero in range(numero_es2):
        lista_es2.append(numero)

    max_lista_es2 = max(lista_es2)

    lista_es2range = range(max_lista_es2, 0, -1)

    for numeri in lista_es2range:
        print(numeri)
    
    decisione = input("Vuoi continuare? Scegli S o N ")
    if decisione.lower() == "s":
        pass
    elif decisione.lower() == "n":
        print: ("Allora ciao!")
        controllore = False
    else:
        print("Scelta non valida")




# Es. 3 for
# Ciclo per aggiungere alla lista, poi esci. 
# Uso ciclo for i in lista, stampa(i**2)

lista_es3 = []
controllore = True

#Ciclo while per inserire numeri nella lista
while controllore:
     numero_da_aggiungere = int(input("Scrivi un numero da aggiungere alla lista: "))
     lista_es3.append(numero_da_aggiungere)
     decisione = input("Vuoi aggiungere un altro numero? Scegli S o N: ")
     if decisione.lower() == "s":
          pass
     elif decisione.lower() == "n":
          print("Fermiamoci qui! Ecco la tua lista: ", lista_es3, ".")
          controllore = False
     else:
          print("Scelta non valida")
          pass     
          
#ciclo for per stampare il quadrato dei numeri
for numero in lista_es3:
     print(numero**2)
 
     


# Es. 4 if + while + for
# Lista input di numeri interi. For per trovare il Max, while per contare i numeri, if per lista vuota oppure num max e num min.
    
###### Inserisco tutti i valori insieme, codice molto piu' snello


lista_es4 = []
valore_es4 = 0
controllore = True
max_lista_es4 = 0
counter_numeri = 0

numeri_da_aggiungere = int(input("Quanti valori vuoi aggiungere? "))

# Ciclo while per inserire numeri nella lista
while numeri_da_aggiungere >0 :
     valore_es4 = int(input("Aggiungi un valore per la lista: "))
     lista_es4.append(valore_es4)
     numeri_da_aggiungere -= 1
     
for numeri in lista_es4:
     max_lista_es4 = max(lista_es4)


# while per contare i numeri,     
while counter_numeri < len(lista_es4):
     counter_numeri += 1

print("La lista e' compsota da ", counter_numeri, " numeri.")

# if per lista vuota oppure num max e num min.
if len(lista_es4) == 0:
     print("La lista e' vuota.")
elif len(lista_es4) != 0:
     print("Il numero massimo e' ", max(lista_es4), " ed il numero minimo e' ", min(lista_es4))
else:
     print("C'e' un errore!")
     
 
     
 

