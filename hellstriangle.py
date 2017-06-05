def valid_struct_triangle(func):
    def valid(triangle):
        size = 0
        for array in triangle:
            size += 1
            if not len(array) == size:
                raise ValueError("Triangle Struct Invalid")
        return func(triangle)
    return valid


def max_nearest_element(index, array):
    if len(array) > 1:
        return max(array[index], array[index+1])
    return array[0]


@valid_struct_triangle
def maximum_top_to_bottom(triangle):
    index = 0
    elements = triangle[0]
    for array in triangle[1:]:
        elements.append(max_nearest_element(index, array))
        index = array.index(elements[-1])
    return sum(elements)
