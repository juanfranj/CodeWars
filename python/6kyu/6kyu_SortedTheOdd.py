def sort_array(source_array):
    impar = sorted([i for i in source_array if i%2 != 0], reverse = True)
    for i in range(0, len(source_array)):
        if source_array[i]%2 != 0:
            source_array[i] = impar.pop()
    return source_array

if __name__ == '__main__':
    a = [5, 3, 2, 8, 1 ,4]
    resultado = sort_array(a)
    print(resultado)
    
# Solucion optima
# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]


''' 
Para practicar:
Metodo para crear un diccionario con las posiciones de los pares e impares  
def posiciones(source_array):
    dic_par = {}
    dic_impar = {}
    for i in range(0,len(source_array)):
        if source_array[i] not in dic_par.keys() and source_array[i]%2==0 :
            dic_par[source_array[i]] = i
        else:
            dic_impar[source_array[i]] = i
    return dic_par, dic_impar
''' 