import random

def insertion_sort(list, iterations=0):
    for index in range(1, len(list)):# Goes over the list
        #* Saves the actual valor and position of the index
        actual_valor = list[index]
        actual_position = index
        # If it isn't in the first position and the element before is bigger than the actual
        while actual_position > 0 and list[actual_position -1 ] > actual_valor:
            #* The valor is given to the actual_valor and goes back to the position before
            list[actual_position] = list[actual_position -1]
            actual_position -= 1

            iterations += 1 # This is just a counter
        list[actual_position] = actual_valor

    return (list, iterations)

if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)

    (list_sorted, iterations) = insertion_sort(list)
    print(list_sorted)
    print(f'Iteraciones de inserción: {iterations}')