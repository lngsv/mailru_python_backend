'CustomList implementation'


class CustomList(list):
    '''
    CustomList implements:
        * element-wise addition and subtraction of lists
        * sum-wise comparison

    CustomList is supposed to contain only numeric elements
    '''

    def __add__(self, other):
        # self and other are supposed to have only numeric elements
        return CustomList(
                self.get_list_element(self, i) +
                self.get_list_element(other, i)
                for i in range(max(len(self), len(other))))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        # self and other are supposed to have only numeric elements
        return CustomList(
                self.get_list_element(self, i) -
                self.get_list_element(other, i)
                for i in range(max(len(self), len(other))))

    def __rsub__(self, other):
        return CustomList(other) - self

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    @staticmethod
    def get_list_element(lst, idx):
        'Returns lst element on idx position (default 0)'
        return lst[idx] if idx < len(lst) else 0
