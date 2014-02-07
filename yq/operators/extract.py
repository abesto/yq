class Extract(object):
    def apply(self, data):
        assert len(data) == 1
        item = data[0]
        if isinstance(item, dict):
            return item.values()
        return item

