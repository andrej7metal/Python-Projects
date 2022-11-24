class cachorro:
    def __init__(self, SRD, CRD):
        self.SRD = SRD
        self.CRD = CRD
    pass
raca1 = cachorro('vira-lata', 'caramelo')
raca2 = cachorro('Puro', 'vacinado', )
print(raca1.SRD, raca1.CRD)
print(raca2.SRD, raca2.CRD)