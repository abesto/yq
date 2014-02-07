from pyparsing import *
from yq.operators.comprehension import Comprehension
from yq.operators.dot import Dot
from yq.operators.projection import Projection, ProjectionItem
from yq.operators.sequence import Sequence
from yq.operators.subscript import Subscript
from yq.operators.subsequence import Subsequence


def parse(str):
    return piped.parseString(str, True).asList()[0]


def wtf(ts):
    import pdb; pdb.set_trace()


key = lambda: Word(alphanums + '_')


operation = Forward()

emptyDot = Literal('.').setParseAction(lambda ts: Dot())
dot = (('.' + key()).setParseAction(lambda ts: Dot(ts[1])) |
       ('["' + key() + '"]').setParseAction(lambda ts: Dot(ts[1])))

subscript = ('[' + Word(nums) + ']').setParseAction(lambda ts: Subscript(int(ts[1])))
subsequence = ('[' + Optional(Word(nums + '-'), None) + ':' + Optional(Word(nums + '-'), None) + ']').setParseAction(lambda ts: Subsequence(ts[1], ts[3]))

chainable = OneOrMore(dot | emptyDot | subscript | subsequence).setParseAction(lambda ts: Sequence(ts.asList()))

projectionItem = (
    (key() + ':' + chainable).setParseAction(lambda ts: ProjectionItem(ts[0], ts[2])) |
    key().setParseAction(lambda ts: ProjectionItem(ts[0], Dot(ts[0])))
)
projection = ('{' + delimitedList(projectionItem, ',') + '}').setParseAction(lambda ts: Projection(ts[1:-1]))

comprehension = ('[' + operation + ']').setParseAction(lambda ts: Comprehension(ts[1]))

operation << (chainable | projection | comprehension)

piped = delimitedList(operation, '|').setParseAction(lambda ts: Sequence(ts.asList()))

