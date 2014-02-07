from yq.operators.base import Operator
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError


class ProjectionItem(object):
    def __init__(self, key, op):
        self.key = key
        self.op = op


class Projection(Operator):
    def __init__(self, items):
        self.items = items

    def _apply_item(self, data):
        retval = {}
        for item in self.items:
            retval[item.key] = item.op._apply_item(data)
        return retval

    def __repr__(self):
        str_items = []
        for item in self.items:
            if isinstance(item.op, Dot) and item.op.key == item.key:
                str_items.append(item.key)
            else:
                str_items.append('%s: %s' % (item.key, item.op))
        return '{' + ', '.join(str_items) + '}'
