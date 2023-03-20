def Minimocomunmultiplo(num1, num2):
    # defino cual es mas grande y lo tomo de referencia 
    if num1 > num2:
        Referente = num1
    else:
        Referente = num2
    while True:
        if Referente % num1 == 0 and Referente % num2 == 0:
            mcm = Referente
            break
        Referente += 1 

    return mcm
print(Minimocomunmultiplo(4,10)) #Un print para testear si funciona 