
v = "ciao"

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
        autore = input("Autore:" )
        numero_pag = input("Numero p.: ")
        titolo = input("Titolo: ")
        aggiunta = Libro(autore, numero_pag, titolo) ##prendo dalla classe di sopra, devo inserire gli argomenti!
        self.lista_libri.append(aggiunta)
        
    def stampa_libro(self):
        # print(self.lista_libri[0].autore, self.lista_libri[0].numero_pag, self.lista_libri[0].titolo)  ##Questo stampa sempre il primo!
        for x in self.lista_libri:  #per stampare ogni libro
            x.stampa_dati()
        
biblio = Biblioteca()
    
while True:
    biblio.crea_libro()
    biblio.stampa_libro()
    
    scelta = input("Vuoi continuare? S/N")
    if scelta == "n":
        break
    
