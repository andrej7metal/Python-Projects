class carro:
    def __init__(self, ford, volks, caoa):
        self.nacional = ford
        self.importado = volks
        self.china = caoa
        pass
modelo1 = carro("fusion","azul", "5p")
modelo2 = carro('mercedes',"prata", '5p')
modelo3 = carro('cherry','preto', '3p')
print(modelo1.nacional, modelo1.importado, modelo1.china)
print(modelo2.nacional, modelo2.importado, modelo2.china)
print(modelo3.nacional, modelo3.importado, modelo3.china) 