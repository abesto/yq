from yq.operators.base import Operator


class Subsequence(Operator):
    def __init__(self, low, hi):
        if low is None:
            self.low = low
        else:
            self.low = int(low)
        if hi is None:
            self.hi = None
        else:
            self.hi = int(hi)

    def _apply_item(self, data):
        try:
            return data[self.low:self.hi]
        except IndexError:
            return None

    def __repr__(self):
        return '[%s:%s]' % (self.low, self.hi)

