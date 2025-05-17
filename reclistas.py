
#haga una funcion que obtenga la suma de los elementos de una lista
def sumaLista(arr):
    if len(arr)>0:
        suma(arr, len(arr)-1)
    else:
        return 0
    
def suma(arr, x) -> int:
    if x == 0:
        return arr[0]
    else: 
        return arr[x] + suma(arr, x-1)
    
def suma2(arr,x,n)->int:
    if x==n:
        return arr[n]
    else:
        return arr[x]+ suma2(arr, x+1)
    
    
lista =[8,6,7]
z=sumaLista(lista)
print(z)

'''
crear una funcion recursiva que me de 
la resta de la suma de los pares menos los impares de una lista
'''