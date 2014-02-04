import yaml


class MatchError(ValueError):
    def __init__(self, operator, data, error):
        self.operator = operator
        self.data = data
        self.error = error
        self.message = 'Failed to apply "%s": %s. The data being processed was:\n%s' % (operator, error, yaml.dump(data))

    def __str__(self):
        return self.message
