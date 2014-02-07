from yq.operators.base import Operator


class Sequence(Operator):
    def __init__(self, operators):
        self.operators = operators

    def _apply_item(self, data):
        for operator in self.operators:
            data = operator._apply_item(data)
        return data

    def __repr__(self):
        return ''.join([repr(operator) for operator in self.operators])
