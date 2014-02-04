from pyparsing import *
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence


def parse(str):
    return sequence.parseString(str, True).asList()[0]

emptyDot = Literal('.').setParseAction(lambda ts: Dot())
dot = ('.' + Word(alphanums + '_')).setParseAction(lambda ts: Dot(ts.asList()[1]))


sequence = OneOrMore(dot | emptyDot).setParseAction(lambda ts: Sequence(ts.asList()))
