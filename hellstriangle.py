def valid_struct_triangle(triangle):
    size = 0
    for array in triangle:
        if not len(array) == size + 1:
            raise ValueError("Triangle Struct Invalid")
        size += 1
    return True


def max_nearest_element(index, array):
    if len(array) > 1:
        return max(array[index], array[index+1])
    return array[0]


def maximum_top_to_bottom(triangle):
    index = 0
    elements = triangle[0]
    for array in triangle[1:]:
        elements.append(max_nearest_element(index, array))
        index = array.index(elements[-1])
    return sum(elements)
