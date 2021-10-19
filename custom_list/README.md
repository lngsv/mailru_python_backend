## CustomList

### To see in python terminal
`custom_list > python3 -i main.py`

### Implements element-wise addition and subtraction
```python
>>> CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
[6, 3, 10, 7]
>>> CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
[4, -1, -4, 7]
```

### One of the operands may be a built-in list
```python
>>> CustomList([5, 1, 3, 7]) + [1, 2, 7]
[6, 3, 10, 7]
>>> [5, 1, 3, 7] - CustomList([1, 2, 7])
[4, -1, -4, 7]
````

### CustomList objects are compared by sum
```python
>>> CustomList([0, 10]) > CustomList([4, 3, 2])
True
>>> [1, 2, 3, 4] == CustomList([10])
True
```

### Run tests
`custom_list > python3 test.py`
