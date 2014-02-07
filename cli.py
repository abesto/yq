#!/usr/bin/env python

import yaml
import sys

from yq import parser
from yq.operators.match_error import MatchError
from yq.output import output


def main(op_str, input):
    op = parser.parse(op_str)
    data = yaml.load(input)
    try:
        for item in op.apply([data]):
            yield item
    except MatchError as ex:
        print ex


if __name__ == '__main__':
    op = sys.argv[1]
    input = sys.stdin.read()
    for item in main(op, input):
        print output(item)
