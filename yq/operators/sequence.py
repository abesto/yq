from yq.operators.base import Operator


class Sequence(Operator):
    def __init__(self, operators):
        self.operators = operators

    def apply(self, data):
        for operator in self.operators:
            data = operator.apply(data)
        return data

    def __repr__(self):
        return ''.join([repr(operator) for operator in self.operators])
