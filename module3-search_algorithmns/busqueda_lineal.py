import random

def lineal_search(list, objective):
    match = False

    for element in list: # O(n) its algorithmic complexity is lineal
        if element == objective:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('De que tamaño sera la lista? '))
    objective = int(input('Que numero quieres encontrar? '))

    list = [random.randint(0, 100) for i in range(list_size)]

    found = lineal_search(list, objective)
    print(list)
    print(f'\nEl elemento {objective} {"esta" if found else "no esta"} en la lista')