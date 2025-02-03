class Contatore:
    numero_istanze = 0  # Attributo di classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
        
# Creazione di alcune istanze

c1 = Contatore()
c2 = Contatore()



##prova classe con vari metodi
class Pippo:
    aumento = 0
    
    #metodo di istanza. Il piu' facile
    def saluta():
        print("ciao Mirko")
       
    #metodo di classe. Operano sulla classe e non su un'istanza specifica. Se cambio qualcosa con questo metodo, lo cambio per le istanze create da ora in poi. 
    @classmethod
    def aumenta():
        Pippo.aumento += 1
        print(Pippo.aumento)
    
    #metodo statico. Non serve un oggetto!
    @staticmethod
    def somma(a,b):
        return a + b
    
p = Pippo()

p.saluta()

p.aumenta()
Pippo.aumenta()

x = Pippo.somma(2,4)



###esercizio 1 slide 119

class Punto:
    x = 0
    y = 0
    def muovi_punto(self, nuovo_x, nuovo_y):
        self.x = nuovo_x
        self.y = nuovo_y
        print("Il nuovo x e' ", nuovo_x, " ed il nuovo y e' ", nuovo_y)
    
    def distanza_da_orgiine(self):
        if self.x != 0 and self.y != 0:
            print("La distanza di X e Y da 0 e' ", self.x, ", ", self.y)
            

roma = Punto() ##NB devi sempre creare un'istanza!
roma.muovi_punto(5, 6)
roma.distanza_da_orgiine()



###Crea una classe chiamata Libro.
# Questa classe dovrebbe avere: Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
        
class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print("Il libro ", self.titolo, " e' stato scritto da ", self.autore, " ed ha ", self.pagine, " pagine.")
        
stargirl = Libro("Stargirl", "Jerry Spinelli", 230)
stargirl.descrizione()

##esercizio slide 120, Libro

class Libro:
    autore = ""
    numero_pag = 0
    titolo = ""
    
    def __init__(self, autore, numero_pag, titolo):
        self.autore = autore
        self.numero_pag = numero_pag
        self.titolo = titolo
        
    def stampa_dati(self):
        print(self.autore, self.numero_pag, self.titolo)

class Biblioteca:
    lista_libri = []
    
    def crea_libro(self):
        autore = input()
        numero_pag = input()
        titolo = input()
        aggiunta = Libro() ##prendo dalla classe di sopra, devo inserire gli argomenti!
        self.lista_libri.append(aggiunta)
        
    def stampa_libro(self):
        # print(self.lista_libri[0].autore, self.lista_libri[0].numero_pag, self.lista_libri[0].titolo)  ##Questo stampa sempre il primo!
        for x in self.lista_libri:  #per stampare ogni libro
            print(x.stampa_dati())
        
biblio = Biblioteca()
    
while True:
    biblio.crea_libro()
    biblio.stampa_libro()
    
    scelta = input("Vuoi continuare? S/N")
    if scelta == "n":
        break
    





##esercizio slide 121, Ristorante

class Ristorante:
    apertura = False
    menu = {}
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def descrivi_ristorante(self):
        print("Il ristorante si chiama ", self.nome, " e la cucina e' ", self.tipo_cucina)
    def stato_apertura(self, apertura):
        self.apertura = apertura
        if apertura == False:
            print("Il ristorante e' chiuso")
        else:
            print("Il ristorante e' aperto")
    def apri_ristorante(self, apertura):
        self.apertura = True
    def chiudi_ristorante(self, apertura):
        self.apertura = False
        print("Il ristorante e' chiuso!")
    #def aggiungi_menu(self, nuova_chiave, nuovo_valore):
    #    self.menu = self.menu{[nuova_chiave], nuovo_valore}
    def rimuovi_menu(self, chiave_rimuovi):
        del self.menu[chiave_rimuovi]
    def stampa_menu(self):
        print("Il menu' e' ", self.menu)
        
diavolo = Ristorante("Il diavolo", "romana")
diavolo.descrivi_ristorante()