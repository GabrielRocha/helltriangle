def valid_struct_triangle(func):
    def valid(triangle):
        size = 0
        for array in triangle:
            size += 1
            if not len(array) == size:
                raise ValueError("Triangle Struct Invalid")
        return func(triangle)
    return valid