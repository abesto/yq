#!/usr/bin/env python

import yaml
import sys

from yq import parser
from yq.output import output

op = parser.parse(sys.argv[1])
input = sys.stdin.read()
data = yaml.load(input)
print output(op.apply(data))
