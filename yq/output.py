import yaml


def output(o):
    if isinstance(o, str):
        return o
    return yaml.dump(o)
