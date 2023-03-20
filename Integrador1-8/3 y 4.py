def Cantidad_de_cada_palabra(string):
    Palabras = string.split()
    Diccionario_de_frecuencias = {}
    for word in Palabras:
        if word in Diccionario_de_frecuencias:
            Diccionario_de_frecuencias[word] += 1
        else:
            Diccionario_de_frecuencias[word] = 1
    return Diccionario_de_frecuencias
def Cual_sale_mas(Diccionario_de_frecuencias):
    RepetidaxVeces = 0
    for word, count in Diccionario_de_frecuencias.items():
        if count > RepetidaxVeces:
            Cual_sale_repetida = word
            RepetidaxVeces = count
    return (Cual_sale_repetida, RepetidaxVeces)
    #Un print para testear si funciona 
test="Este Este Este este no NO es un buen test ya que todas las palabras aparecen solo una vez"
Dicc_de_test={'Este': 3, 'este': 1, 'no': 1, 'NO': 1, 'es': 1, 'un': 1, 'buen': 1, 'test': 1, 'ya': 1, 'que': 1, 'todas': 1, 'las': 1, 'palabras': 1, 'aparecen': 1, 'solo': 1, 'una': 1, 'vez': 1}
print(Cantidad_de_cada_palabra(test))
print(Cual_sale_mas(Dicc_de_test))