import hellstriangle
import pytest


def test_valid_struct_triangle():
    example = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    assert hellstriangle.valid_struct_triangle(example)


def test_invalid_struct_triangle():
    example = [[6], [3, 5], [9, 7], [4, 6, 8, 4]]
    with pytest.raises(ValueError) as error:
        hellstriangle.valid_struct_triangle(example)
    assert "Triangle Struct Invalid" == str(error.value)
