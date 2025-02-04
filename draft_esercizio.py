#classe computer che ha come padre processore (velocita') e RAM (memoria)
class Processore:
    def __init__(self, tipo_processore, velocita):
        self.tipo_processore = tipo_processore
        self.velocita = velocita
    
    def sistema_supportato():
        print("I nuovi processori supportano solo sistemi operativi rilasciati dal 2020 in poi.")
        
    def stampa_info_processore(self):
        print("Le informazioni del processore sono: ", self.tipo_processore, self.velocita)
    
class Ram:
    def __init__(self, memoria):
        self.memoria = int(memoria)
    
    def aumento_ram(self):
        if self.memoria < 100:
            print("Questa RAM puo' essere estesa, devi acquistare un'estensione!")
            
    def stampa_info_ram(self):
        print("Le informazioni della ram sono: ", self.memoria)
    
class Computer(Processore, Ram):
    def __init__(self, tipo_processore, velocita, memoria, linguaggio_computer):
        Processore.__init__(self, tipo_processore, velocita)
        Ram.__init__(self, memoria)
        self.linguaggio_computer = linguaggio_computer
       
    def tipo_tastiera(self):
        if self.linguaggio_computer == "eng":
            print("La tastiera ha la formattazione inglese")
        elif self.linguaggio_computer == "it":
            print("La tastiera ha la formattazione inglese ")
        else:
            print("Formattazione non riconosciuta o inserimento non valido.")
            
    def stampa_informazioni(self):
        Processore.stampa_info_processore(self)
        Ram.stampa_info_ram(self)
        
            
computer1 = Computer("Intel", "Super", "100", "eng")
computer1.stampa_informazioni()
computer1.tipo_tastiera()