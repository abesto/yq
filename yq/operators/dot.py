from yq.operators.base import Operator
from yq.operators.match_error import MatchError


class Dot(Operator):
    def __init__(self, key=''):
        self.key = key

    def _apply_item(self, data):
        if self.key == '':
            return data
        if not isinstance(data, dict):
            raise MatchError(self, data, 'tried to access field %s on a non-object' % self)
        try:
            return data[self.key]
        except KeyError:
            return None

    def __repr__(self):
        return '.%s' % self.key
