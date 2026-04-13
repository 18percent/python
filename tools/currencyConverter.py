# Write code below 💖
def start():
    pesos = int (input ("pesos left "))
    soles = int (input ("soles left "))
    reais = int (input ("reais left "))

    usd_to_pesos = 0.00027
    usd_to_soles = 0.29
    usd_to_reais = 0.19

    usd_pesos = pesos * usd_to_pesos
    usd_soles = soles * usd_to_soles
    usd_reais = reais * usd_to_reais

    print ("usd left", usd_pesos + usd_soles + usd_reais)