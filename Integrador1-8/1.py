def MCD(num1, num2):
    # Esta primer parte los da vuelta en caso de 2 ser mayor a 1
    if num2 > num1:
        num1, num2 = num2, num1

    while num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    return num1
print (MCD(120,45)) #Un print para testear si funciona 