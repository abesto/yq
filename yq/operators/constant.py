from yq.operators.base import Operator


class Constant(Operator):
    def __init__(self, value):
        self.value = value

    def apply(self, _):
        return self.value

    def __repr__(self):
        return str(self.value)

