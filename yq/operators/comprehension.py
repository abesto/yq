from yq.operators.match_error import MatchError


class Comprehension(object):
    def __init__(self, op):
        self.op = op

    def apply(self, data):
        if not isinstance(data, list):
            raise MatchError(self, data, 'tried to apply comprehension %s to non-array' % self)
        retval = []
        for item in data:
            retval.append(self.op.apply(item))
        return retval

    def __repr__(self):
        return '[%s]' % self.op
