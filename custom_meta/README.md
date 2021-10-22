## CustomMeta

### To see in python terminal
`custom_meta $ python3 -i main.py`

### Implements metaclass that adds 'custom_' prefix to all (non-magic) methods
```python
>>> class CustomClass(metaclass=CustomMeta):
...     x = 99
...     def __init__(self):
...             self.val = 15
...     def line(self):
...             return 100
... 
>>> inst = CustomClass()
>>> inst.custom_x
99
>>> inst.custom_val
15
>>> inst.custom_line()
100
>>> inst.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'CustomClass' object has no attribute 'x'
>>> inst.val
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'CustomClass' object has no attribute 'val'
>>> inst.line()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'CustomClass' object has no attribute 'line'
```


### Run tests
`custom_meta $ python3 test.py`
