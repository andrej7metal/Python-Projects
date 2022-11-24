def fazer_big_mac (nome):
    print(f"sanduiche big mac {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante (tipo,tamanho):
    print(f"{tipo}, tamanho: {tamanho}")

def fazer_combo_big_mac (nome,batata_tamanho,tipo_refrigerante,tamanho_refrigerante):
    fazer_big_mac(nome) 
    fazer_batata(batata_tamanho)
    preparar_refrigerante(tipo_refrigerante,tamanho_refrigerante)
    return fazer_big_mac, fazer_batata, preparar_refrigerante, fazer_combo_big_mac
pedido = fazer_combo_big_mac("juvenal","médio","sprite","pequeno")

#print(fazer_combo_big_mac)
#fazer_big_mac(fazer_combo_big_mac)
#fazer_batata("média")
#preparar_refrigerante("coca-cola","Grande")  
#fazer_combo_big_mac("Ania","média","coca","grande")  # o programa em execução nao retorna nada no terminal



