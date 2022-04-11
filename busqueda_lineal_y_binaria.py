import random

def lineal_search(list, objective, iterations_lin=0):
    match = False

    for element in list: # O(n) its algorithmic complexity is lineal
        iterations_lin += 1
        if element == objective:
            match = True
            break

    return match, iterations_lin


def binary_search(list, beginning, end, objective, iterations_bin=0):
    iterations_bin +=1
    if beginning > end:
        return (False, iterations_bin)

    middle = (beginning + end) // 2

    if list[middle] == objective:#* The algorithm determines that the objective isn't this iteration
        return (True, iterations_bin)
    elif list[middle] < objective: # The algorithm goes up in the list
        return binary_search(list, middle + 1, end, objective, iterations_bin)
    else: # The algorithm goes down in the list
        return binary_search(list, beginning, middle - 1, objective, iterations_bin)


if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))
    objective = int(input('Que numero quieres encontrar? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    (found, iterations_lin) = lineal_search(list, objective)
    (found, iterations_bin) = binary_search(list, 0, len(list), objective)
    print(list)
    print(f'El elemento {objective} {"esta" if found else "no esta"} en la lista')

    print(f'Iteraciones busqueda lineal {iterations_lin}')
    print(f'Iteraciones busqueda binaria: {iterations_bin}')