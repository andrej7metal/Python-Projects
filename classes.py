class macdonald:
   def __init__(self, lanche, suco):
       self.lanche = lanche # este nome lance é declarado na variavel print la em baixo
       self.suco = suco
pedido = macdonald("Big King","Suco_uva")
print(pedido.lanche, pedido.suco) # nao pode por só a variavel pedido e esquecer o .lanche
