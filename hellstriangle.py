from validate import valid_struct_triangle
import random


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


def generate_random_triangle(steps=2):
    len_elements_list = 1
    triangle = list()
    for i in range(steps):
        triangle.append([random.randint(1, 10) for index in range(len_elements_list)])
        len_elements_list += 1
    return triangle
