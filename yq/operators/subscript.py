from yq.operators.base import Operator


class Subscript(Operator):
    def __init__(self, index):
        assert isinstance(index, int)
        self.index = index

    def _apply_item(self, data):
        # TODO: check that data is a list
        try:
            return data[self.index]
        except IndexError:
            return None

    def __repr__(self):
        return '[%s]' % self.index

