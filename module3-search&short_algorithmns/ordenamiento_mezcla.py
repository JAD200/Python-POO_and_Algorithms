import random



def mixture_sort(list):

    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        print(left, '*' * 5, right)

        #* Recursive call in every middle
        mixture_sort(left)
        mixture_sort(right)

        #* Iterators to go over two sublists
        i = 0
        j = 0

        #* iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k +=1

        while i < len(left):
            list[k] = left[i]
            i +=1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j +=1
            k += 1

        print(f'Izquierda: {left}, derecha: {right}')
        print(list)
        print('-' * 50)
    return list


if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)
    print('_ ' * 20)

    list_sorted = mixture_sort(list)
    print(list_sorted)
    # print(f'Iteraciones de mezcla: {iterations}')