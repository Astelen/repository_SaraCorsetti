
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
        
        def __metodo_privato(self):
            return "Questo e' un metodo privato"
        
        def __pippo_privato(self):
            print("Ciao")
            
        def __pippo_privato(self):
            print(__metodo_privato)
        
obj = MiaClasse()
# se stampo print(obj.__variabile_privata) ottengo un errore!! AttributeError
print(obj._MiaClasse__variabile_privata) # questo funziona MA NON SI FA.



#####

##esercizio scuola slide 154

class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta
    
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    def set_nome(self, nuovo_nome):
        if self.__nome != "":
            self.__nome = nuovo_nome
    
    def set_eta(self, nuova_eta):
        if self.__eta != 0:
            self.__eta = nuova_eta
    
    def presentazione(self):
        print("Il nome e': ", self.__nome, ", l'eta' e': ", self.__eta)

class Studente(Persona):     #NB con get posso evitare di fare l'init! Basta che faccio def get.nome e def get.eta INVECE del costruttore.
        #In questo caso devo mettere per forza il setter per modificarlo. In questo caso posso mettere privati
        # i dati anche nel padre
    __voti = []
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        if len(self.__voti) != 0:
            self.__voti = voti #posso inserire un ciclo e mettere tipo quanti voti hai? poi li inserisco in una lista e lo passo come parametro. Da fare nel menu'
        else:
            self.__voti = 0
        
    def calcola_media(self):
        somma = 0
        print(self.__voti)
        if len(self.__voti) > 0: #sto ciclo If non serve davvero
            for x in self.__voti:
                somma += x
            return somma/len(self.__voti)
        else:
            return "La media e' 0"
     
    def presentazione(self):
        print("Il nome e': ", self.__nome, ", l'eta' e': ", self.__eta, ", la media dei voti e': ", self.calcola_media())
        
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
        
    def presentazione(self):
        print("Il nome e': ", self.__nome, ", l'eta' e': ", self.__eta, ", la materia di ineagnamento e': ", self.__materia)
        
        
     
persona1 = Persona("Marco", 34)
print(persona1.get_nome())
print(persona1.get_eta())
persona1.set_nome("Antonio")
persona1.set_eta(56)
print(persona1.get_nome())
print(persona1.get_eta())
persona1.presentazione()

studente1 = Studente("Sara", 37, [28, 30, 19])
studente2 = Studente("Luca", 28, [28, 30, 30])
print(studente1.get_nome())
print(studente1.get_eta())
print(studente2.get_nome())
print(studente2.get_eta())
studente2.calcola_media()
