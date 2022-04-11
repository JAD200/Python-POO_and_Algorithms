import random

def binary_search(list, beginning, end, objective):
    print(f'Buscando el {objective} entre {list[beginning]} y {list[end - 1]}')
    if beginning > end:
        return False

    middle = (beginning + end) // 2

    if list[middle] == objective:#* The algorithm determines that the objective isn't this iteration
        return True
    elif list[middle] < objective: # The algorithm goes up in the list
        return binary_search(list, middle + 1, end, objective)
    else: # The algorithm goes down in the list
        return binary_search(list, beginning, middle - 1, objective)


if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))
    objective = int(input('Que numero quieres encontrar? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list, 0, len(list), objective)
    print(list)
    print(f'El elemento {objective} {"esta" if found else "no esta"} en la lista')