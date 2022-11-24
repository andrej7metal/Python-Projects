def fazer_bic_mac(nome):
    print(f"sanduiche big mac {nome}")

def fazer_batata(tamanho):
    print(f"Batata frita{tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo}{tamanho}")


#fazer_bic_mac("joao")     
#fazer_batata("grande")
#preparar_refrigerante("coca","grande")

def fazer_combo(nome,batata_tamanho,refri_tipo,refri_tamanho):
    fazer_bic_mac(nome)
    fazer_batata(batata_tamanho) 
    preparar_refrigerante(refri_tipo,refri_tamanho)          # as 3 linhas acima deve estar no meio da DEF e fazer_combo() igual abaixo


fazer_combo("juvenal"," grande","medio ","laranja")  # esta linha deve estar colada na parede <= para funcionar
