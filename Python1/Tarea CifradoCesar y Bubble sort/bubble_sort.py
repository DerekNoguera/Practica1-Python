
def bubble_sort(array):

    lista = len(array)
    for i in range(lista):
        for j in range(lista - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
array_listado = [5,4,2,7,1]
bubble_sort(array_listado)
print(array_listado)
