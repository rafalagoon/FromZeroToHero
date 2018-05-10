
def calculaIVA (lootbox):
    iva = 0.21

    lootbox_iva = lootbox + lootbox*iva
    
    return lootbox_iva


print("El IVA de tu lootbox es:", calculaIVA(120))
