def morral(morral_size, weights, values, n):
    """morral Add elements to a bag with a certain size

    Args:
        morral_size (int): Size of the bag
        weights (int): # Weight of the elements
        values (int): # Value of each element
        n (int): # Index of elements to select

    Returns:
        int: Three statements
        1. If there aren't more elements or there isn't more bag size
            return 0

        2. If the element weight to include is more than the current bag size
            return morral(morral_size, weights, values, n -1)

        3. Decision for weather select the current object or not and change morral size and n values
            return max(values[n -1] +morral(morral_size - weights[n - 1], weights, values, n - 1),
                morral(morral_size, weights, values, n - 1))
    """
    if n == 0 or morral_size == 0:
        print('Valor n:', n, '-' * 4, 'Espacio tomado morral:', morral_size)
        return 0

    if weights[n -1] > morral_size:
        print('Valor n:', n, '/' * 3, 'Espacio morral:', morral_size)
        return morral(morral_size, weights, values, n -1)

    return max(values[n -1] +morral(morral_size - weights[n - 1], weights, values, n - 1),
                morral(morral_size, weights, values, n - 1))



if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    morral_size = 50
    n = len(values)

    result = morral(morral_size, weights, values, n)
    print(result)