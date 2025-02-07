from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
        
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
#classe derivata ImpiegatoFisso
class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base
    
    def __str__(self):
        return f"Ecco i dati dell'impiegato: {self.nome}, {self.cognome}, {self.calcola_stipendio()}"

#classe derivata ImpiegatoProvvigione:
class ImpiegatoProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base + (self.stipendio_base*4)/100
    
    def __str__(self):
        return f"Ecco i dati dell'impiegato: {self.nome}, {self.cognome}, {self.calcola_stipendio()}"
    
imp1 = ImpiegatoFisso("Andrea", "De Santis", 100)
print(imp1.calcola_stipendio())
print(imp1.calcola_stipendio())

imp3 = ImpiegatoProvvigione("Valerio", "Leo", 200)
print(imp3.calcola_stipendio())

print(imp1)
print(imp3)

