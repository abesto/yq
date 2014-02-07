from yq.operators.base import Operator


class Subscript(Operator):
    def __init__(self, indices):
        self.indices = indices

    def apply(self, data):
        retval = []
        for i in self.indices:
            try:
                retval.append(data[0][i])
            except IndexError:
                retval.append(None)
        return retval

    def __repr__(self):
        return '[%s]' % ','.join(self.indices)

