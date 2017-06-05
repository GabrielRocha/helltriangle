import hellstriangle
import pytest


@pytest.mark.parametrize("function", [
    hellstriangle.maximum_top_to_bottom,
    hellstriangle.valid_struct_triangle(lambda x: x)
])
def test_decorator_valid_struct_triangle_function(function):
    triangle = [[6], [3, 5], [9, 7], [4, 6, 8, 4]]
    with pytest.raises(ValueError) as error:
        function(triangle)
    assert "Triangle Struct Invalid" == str(error.value)


def test_valid_struct_triangle():
    triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    assert hellstriangle.valid_struct_triangle(lambda x: x)(triangle)
