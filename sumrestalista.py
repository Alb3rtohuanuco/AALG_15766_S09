
'''
def sumaresta():
    pass


lista=[2,3,8,1]
z=sumaresta() #10-4=6
'''
'''
crear una funcion recursiva que me de la 
resta de la suma de los pares menos los impares de una lista
'''


def resta_pares_impares(lista, index=0):
    if index == len(lista):
        return 0
    
    actual = lista [index]
    resultado_resto=resta_pares_impares(lista, index+1)
    
    if actual % 2==0:
        return actual + resultado_resto
    else:
        return -actual+resultado_resto
    
numeros=[2,3,8,1]
resultado = resta_pares_impares(numeros)
print(f"Resultado final 1 : {resultado}")


numeros2=[4,7,9,2,1,8,6]
resultado2 = resta_pares_impares(numeros2)
print(f"Resultado final 2 : {resultado2}")
