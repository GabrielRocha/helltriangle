import hellstriangle
import pytest


def test_valid_struct_triangle():
    triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    assert hellstriangle.valid_struct_triangle(triangle)


def test_invalid_struct_triangle():
    triangle = [[6], [3, 5], [9, 7], [4, 6, 8, 4]]
    with pytest.raises(ValueError) as error:
        hellstriangle.valid_struct_triangle(triangle)
    assert "Triangle Struct Invalid" == str(error.value)


@pytest.mark.parametrize("values", [
    [0, [1, 2, 3, 4, 5], 2],
    [1, [1, 2, 3, 4, 5], 3],
    [2, [1, 2, 3, 4, 5], 4]
])
def test_max_nearest_element(values):
    index, array, result = values
    assert hellstriangle.max_nearest_element(index, array) == result
