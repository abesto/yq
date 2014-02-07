class Operator(object):
    def apply(self, data):
        return map(self._apply_item, data)

    def _apply_item(self, data):
        raise NotImplementedError()