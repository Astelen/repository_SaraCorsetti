
# classe padre MembroSquadra
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def descrizione_membro(self):
        print("Il nome del membro e' :", self.nome,
              "l'eta' del membro e' :", self.eta)

# classe figlio Giocatore
class Giocatore(MembroSquadra):
    def __init__ (self, nome, eta, ruolo):
        MembroSquadra.__init__(self, nome, eta)
        self.ruolo = ruolo
        
    def descrizione_giocatore(self):
        MembroSquadra.descrizione_membro(self)
        print("Il ruolo del giocatore e' :", self.ruolo)
        
    def gioca_partita(self):
        print("Sta per entrare in campo!")

# classe figlio Allenatore
class Allenatore(MembroSquadra):
    def __init__ (self, nome, eta, anni_esperienza):
        MembroSquadra.__init__(self, nome, eta)
        self.anni_esperienza = anni_esperienza
        
    def descrizione_allenatore(self):
        MembroSquadra.descrizione_membro(self)
        print("Ha accumulato questi anni di esperienza come allenatore :", self.anni_esperienza)
        
    def dirige_allenamento(self):
        print("Allenamenti in corso, non disturbare.")
        
# classe figlio Assistente
class Assistente(MembroSquadra):
    def __init__ (self, nome, eta, specializzazione):
        MembroSquadra.__init__(self, nome, eta)
        self.specializzazione = specializzazione
        
    def descrizione_assistente(self):
        MembroSquadra.descrizione_membro(self)
        print("E' specializzato come :", self.specializzazione)
        
    def supporto_allenamento(self):
        print("Supporta l'allenamento come ", self.specializzazione)
        
# classe Squadra, composto da MembroSquadra
class Squadra:
    lista_squadra = []
    lista_giocatori = []
    lista_allenatori = []
    lista_assistenti = []
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra

    def aggiungi_giocatore(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        ruolo = input("Digita il ruolo: ")
        aggiunta_giocatore = Giocatore(nome, eta, ruolo) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_giocatori.append(aggiunta_giocatore)
        
    def aggiungi_allenatore(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        anni_esperienza = input("Digita gli anni di esperienza: ")
        aggiunta_allenatore = Giocatore(nome, eta, anni_esperienza) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_allenatori.append(aggiunta_allenatore)
        
    def aggiungi_assistente(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        specializzazione = input("Digita la specializzazione: ")
        aggiunta_assistente = Giocatore(nome, eta, specializzazione) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_assistenti.append(aggiunta_assistente)
    
    def __str__(self): #stampa elenco squadre
        return f"Squadra: {self.nome_squadra}, Elenco allenatori: {self.lista_allenatori}, \n elenco giocatori: {self.lista_giocatori}, \n elenco assistenti: {self.lista_assistenti}" 
    
squadra1 = Squadra("Roma")

while True:
    scelta_inserimento = int(input("Scegli 1 per inserire un giocatore, 2 per un allenatore, 3 per un assistente, 4 per uscire."))
    if scelta_inserimento == 1:
        squadra1.aggiungi_giocatore()
    elif scelta_inserimento == 2:
        squadra1.aggiungi_allenatore()
    elif scelta_inserimento == 3:
        squadra1.aggiungi_assistente()
    elif scelta_inserimento == 4:
        scelta_stampa = input("Vuoi stampare la lista della squadra? Scegli S o N: ")
        if scelta_stampa.lower() == "s":
            print(squadra1)
        elif scelta_stampa.lower() == "n":
            print("Ok!")
            break
    else:
        print("Scelta non valida")
