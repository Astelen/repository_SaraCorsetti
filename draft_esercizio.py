class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        
        if titolare != "":
            self.__titolare = titolare
        else:
            self.__titolare = "Sconosciuto"
        
        if saldo_iniziale > 0:
            self.__saldo = saldo_iniziale
        else:
            self.__saldo = 0
    
    #metodo per prelievi e depositi        
    def rinnovo_saldo(self, importo):
        nuovo_saldo = self.__saldo + importo
        if nuovo_saldo >=0:
            self.__saldo = nuovo_saldo
        else:
            print("Prelievo non disponibile")
    
    #stampa saldo
    def visualizza_saldo(self):
        return self.__saldo
    
    def visualizza_titolare(self):
        return self.__titolare
    
    def set_titolare(self, nuovo_titolare):
        if nuovo_titolare != "":
            self.__titolare = nuovo_titolare
    
        
contobancario1 = ContoBancario("Antonio", 1000)  
contobancario1.visualizza_saldo()
contobancario1.rinnovo_saldo(2000)
print("Saldo dopo deposito: ", contobancario1.visualizza_saldo())
print(contobancario1.visualizza_titolare())
contobancario1.set_titolare("Valerio")
print(contobancario1.visualizza_titolare())