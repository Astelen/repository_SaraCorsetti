class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {self.dotazioni}")
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) #richiama questi parametri dalla classe padre Veicolo
        DotazioniSpeciali.__init__(self, dotazioni) #richiama questi parametri dalla classe padre DotazioniSpeciali
        self.cavalli = cavalli #aggiunge questo parametro
    
    def mostra_informazioni(self):
        super().mostra_informazioni()  ##prende da prima classe padre ovvero Veicolo
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        
autosportiva1 = AutomobileSportiva("BMW", "5", "Cruise control", "1500")
autosportiva1.mostra_informazioni()


