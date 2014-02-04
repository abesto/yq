from pyparsing import *
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence
from yq.operators.subscript import Subscript


def parse(str):
    return sequence.parseString(str, True).asList()[0]

emptyDot = Literal('.').setParseAction(lambda ts: Dot())
dot = ('.' + Word(alphanums + '_')).setParseAction(lambda ts: Dot(ts.asList()[1]))

subscript = ('[' + Word(nums) + ']').setParseAction(lambda ts: Subscript(int(ts.asList()[1])))

sequence = OneOrMore(dot | emptyDot | subscript).setParseAction(lambda ts: Sequence(ts.asList()))
