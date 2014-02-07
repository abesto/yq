from yq.operators.match_error import MatchError


class Subscript(object):
    def __init__(self, index):
        assert isinstance(index, int)
        self.index = index

    def apply(self, data):
        if self.index == '':
            return data
        try:
            return data[self.index]
        except IndexError:
            raise MatchError(self, data, 'index "%d" not found' % self.index)

    def __repr__(self):
        return '[%s]' % self.index

