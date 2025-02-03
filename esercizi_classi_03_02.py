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