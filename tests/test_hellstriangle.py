import hellstriangle
import pytest


@pytest.mark.parametrize("values", [
    [0, [1, 2, 3, 4, 5], 2],
    [1, [1, 2, 3, 4, 5], 3],
    [2, [1, 2, 3, 4, 5], 4],
    [0, [1], 1]
])
def test_max_nearest_element(values):
    index, array, result = values
    assert hellstriangle.max_nearest_element(index, array) == result


@pytest.mark.parametrize("values", [
    ([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]], 26),
    ([[6], [10, 5], [9, 7, 1], [4, 6, 8, 4]], 31),
    ([[6], [3, 4], [9, 7, 8], [4, 6, 8, 10]], 28)
])
def test_maximum_helltriangle(values):
    triangle, result = values
    assert hellstriangle.maximum_top_to_bottom(triangle) == result


@pytest.mark.parametrize("steps", [4, 5, 6, 10, 20, 30])
def test_generate_triangle(steps):
    triangle = hellstriangle.generate_random_triangle(steps)
    assert hellstriangle.valid_struct_triangle(lambda x:x)(triangle)
