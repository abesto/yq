class Comma(object):
    def __init__(self, ops):
        self.ops = ops

    def apply(self, data):
        return [item for sublist in [op.apply(data) for op in self.ops] for item in sublist]
