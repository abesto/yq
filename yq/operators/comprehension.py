from yq.operators.base import Operator
from yq.operators.match_error import MatchError


class Comprehension(Operator):
    def __init__(self, op):
        self.op = op

    def _apply_item(self, data):
        if not isinstance(data, list):
            raise MatchError(self, data, 'tried to apply comprehension %s to non-array' % self)
        retval = []
        for item in data:
            retval.append(self.op._apply_item(item))
        return retval

    def __repr__(self):
        return '[%s]' % self.op
