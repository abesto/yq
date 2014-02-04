import yaml


def output(o):
    if isinstance(o, dict) or isinstance(o, list):
        return yaml.dump(o)
    return str(o)

