class CartaDiCredito:
    def effettua_pagamento(self, importo):
        print(importo, "pagato con carta di credito.")

class Paypal:
    def effettua_pagamento(self, importo):
        print(importo, "pagato con carta di credito.") #self solo con qualcosa che appartiene alla classe

class GestionePagamento:
    def __init__(self, metodo_di_pagamento):
        self.metodo_di_pagamento = metodo_di_pagamento
    
    def esegui_pagamento(self, importo):
        self.metodo_di_pagamento.effettua_pagamento(importo)
        
carta1 = CartaDiCredito()
gestione1 = GestionePagamento(carta1)  #creo istanza GestionePagamento chiamata gestione1, il parametro assegno carta1 oggetto di metodo_di_pagamento
gestione1.esegui_pagamento(200)