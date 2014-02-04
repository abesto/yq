#!/usr/bin/env python

import yaml
import sys

from yq import parser
from yq.operators.match_error import MatchError
from yq.output import output

op = parser.parse(sys.argv[1])
input = sys.stdin.read()
data = yaml.load(input)

try:
    print output(op.apply(data))
except MatchError as ex:
    print ex
