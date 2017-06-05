
def valid_struct_triangle(triangle):
    size = 0
    for array in triangle:
        if not len(array) == size + 1:
            raise ValueError("Triangle Struct Invalid")
        size += 1
    return True


def max_nearest_element(index, array):
    return max(array[index], array[index+1])
