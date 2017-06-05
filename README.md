#Hell Triangle - Challenge
Given a triangle of numbers, find the maximum total from top to bottom.

Example:

       6        
      3 5
     9 7 1
    4 6 8 4
    
In this triangle the maximum total is:  6 + 5 + 7 + 8 = 26

An element can only be summed with one of the two nearest elements in the next row. For example: 
The element 3 in the 2nd row can only be summed with 9 and 7, but not with 1

The code will receive an (multidimensional) array as input.

The triangle from above would be:

```python
example = [[6],[3,5],[9,7,1],[4,6,8,4]]
```