
def fazer_bic_mac(nome):
    print(f"sanduiche big mac {nome}")
def fazer_batata(tamanho):
    print(f"Batata frita{tamanho}")
def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo}{tamanho}")
def combo_big_mac(nome,batata_tamanho,refrigerante_tamanho,refrigerante_sabor):
    fazer_bic_mac(nome)            #aqui só declaramos funções não chamamos ainda 
    fazer_batata(batata_tamanho)    #declarando uma função                                
    preparar_refrigerante(refrigerante_tamanho,refrigerante_sabor) #declarando uma função
combo_big_mac("lala","grande","medio","laranja")
    #combo_big_mac("cheddar","grande","pequeno","fanta")  #abaixo agora vamos chamar o combo => combo_big_mac() 




  
    