from yq.operators.match_error import MatchError


class Dot(object):
    def __init__(self, key=''):
        assert isinstance(key, str)
        self.key = key

    def apply(self, data):
        if self.key == '':
            return data
        try:
            return data[self.key]
        except KeyError:
            raise MatchError(self, data, 'key "%s" not found' % self.key)

    def __repr__(self):
        return '.%s' % self.key
