
#esercizio Teatro slide 165, simulazione TEATRO

## Classe Base: Posto
# Attributi privati:
# _numero (intero): il numero del posto.
# _fila (stringa): la fila in cui si trova il posto.
# _occupato (booleano): stato del posto, se è occupato (True) o libero (False).

class Posto:
    def __init__(self, numero_posto, fila_posto, occupato_bool = False): #costruttore con parametri
        self.__numero_posto = numero_posto
        self.__fila_posto = fila_posto
        self.occupato_bool = occupato_bool
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato.")
        else:
            print("Posto gia' occupato, scegline un altro.")
            
    def libera_posto(self): #Disdetta prenotazione che imposta booleano su False
        if self.occupato_bool == True:
            self.occupato_bool = False
            print("Prenotazione disdetta. Il posto ora e' di nuovo libero.")
        else:
            print("Il posto e' gia' libero.")
            
    def get_attributi(self): #recupero attributi dell'ogggetto
        return f"Numero posto: {self.__numero_posto}, fila: {self.__fila_posto}, stato: {self.occupato_bool}."
            
posto_mario = Posto(10, "G", True)    
print(posto_mario.get_attributi())   
posto_mario.libera_posto()
            
class PostoVIP(Posto):
    def __init__(self, numero_posto, fila_posto, occupato_bool, servizi_extra): #costruttore con parametri
        super().__init__(numero_posto, fila_posto, occupato_bool)
        self.__servizi_extra = servizi_extra
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato. Ora puoi scegliere i tuoi servizi extra. Abbiamo disponibile: accesso alla lounge, aperitivo vip.")
            num_scelta_vip = int(input("Quanti servizi vuoi prenotare? Digita 1 o 2: "))
            if num_scelta_vip == 1:
                tipo_scelta_vip = int(input("Digta 1 per l'accesso alla lounge, 2 per l'aperitivo Vip: "))
                if tipo_scelta_vip == 1:
                    print("Hai selezionato l'accesso alla lounge.")
                elif tipo_scelta_vip == 2:
                    print("Hai selezionato l'aperitivo VIP.")
                else:
                    print("Scelta non valida.")
            elif num_scelta_vip == 2:
                print("Ottima scelta!")
            else:
                print("Scelta non valida.")
        else:
            print("Posto gia' occupato, scegline un altro.")

    def get_attributi_vip(self): #recupero attributi dell'ogggetto. 
        #Se riscrivo la get come nel padre mi dice che non abbiamo attributo PostoVIP_numero_posto
        # quindi ho pensato a questa soluzione, chiedere a Mirko se e' giusta
        print(self.get_attributi(), "Servizi aggiuntivi: ", self.__servizi_extra)

posto_mario = PostoVIP(10, "G", True, "accesso lounge")    
posto_mario.get_attributi_vip()
#print(posto_mario.libera_posto())

class PostoStandard(Posto):
    def __init__(self, numero_posto, fila_posto, occupato_bool, servizi_extra): #costruttore con parametri
        super().__init__(numero_posto, fila_posto, occupato_bool)
        self.__servizi_extra = servizi_extra
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato. Ora puoi scegliere i tuoi servizi extra. Abbiamo disponibile: accesso alla lounge, aperitivo vip.")
            num_scelta_vip = int(input("Quanti servizi vuoi prenotare? Digita 1 o 2: "))
            if num_scelta_vip == 1:
                tipo_scelta_vip = int(input("Digta 1 per l'accesso alla lounge, 2 per l'aperitivo Vip: "))
                if tipo_scelta_vip == 1:
                    print("Hai selezionato l'accesso alla lounge.")
                elif tipo_scelta_vip == 2:
                    print("Hai selezionato l'aperitivo VIP.")
                else:
                    print("Scelta non valida.")
            elif num_scelta_vip == 2:
                print("Ottima scelta!")
            else:
                print("Scelta non valida.")
        else:
            print("Posto gia' occupato, scegline un altro.")

    def get_attributi_vip(self): #recupero attributi dell'ogggetto. 
        #Se riscrivo la get come nel padre mi dice che non abbiamo attributo PostoVIP_numero_posto
        # quindi ho pensato a questa soluzione, chiedere a Mirko se e' giusta
        print(self.get_attributi(), "Servizi aggiuntivi: ", self.__servizi_extra)

class Teatro:
    pass #racchiude tutti i posti, sia VIP che Standard