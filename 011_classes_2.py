class computador:
    def __init__(self, modelo, tipo): # coloca aqui modelo tipo do lado do self
        self.modelo = modelo  # tira aspas ' ' aqui se não da erro
        self.tipo = tipo # sem ' ' aspas também
        pass
computador1 = computador('asus', '8gb')
computador2 = computador('mac', '16gb')
print(computador1.modelo, computador1.tipo)
print(computador2.modelo, computador2.tipo)