class Comprehension(object):
    def __init__(self, op):
        self.op = op

    def apply(self, data):
        retval = []
        for item in data:
            retval.append(self.op.apply(item))
        return retval
