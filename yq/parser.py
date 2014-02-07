from pyparsing import *
from yq.operators.comma import Comma
from yq.operators.comprehension import Comprehension
from yq.operators.dot import Dot
from yq.operators.extract import Extract
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

extract = Literal('[]').setParseAction(Extract)

emptyDot = Literal('.').setParseAction(lambda ts: Dot())
dot = (('.' + key()).setParseAction(lambda ts: Dot(ts[1])) |
       ('.["' + key() + '"]').setParseAction(lambda ts: Dot(ts[1])))

subscript = ('[' + delimitedList(Word(nums)) + ']').setParseAction(lambda ts: Subscript(map(int, ts[1:-1])))
subsequence = ('[' + Optional(Word(nums + '-'), None) + ':' + Optional(Word(nums + '-'), None) + ']').setParseAction(lambda ts: Subsequence(ts[1], ts[3]))

chainable = extract | dot | emptyDot | subscript | subsequence
chain = OneOrMore(chainable).setParseAction(lambda ts: Sequence(ts.asList()))

comma = delimitedList(chain).setParseAction(Comma)

projectionItem = (
    (key() + ':' + chain).setParseAction(lambda ts: ProjectionItem(ts[0], ts[2])) |
    key().setParseAction(lambda ts: ProjectionItem(ts[0], Dot(ts[0])))
)
projection = ('{' + delimitedList(projectionItem, ',') + '}').setParseAction(lambda ts: Projection(ts[1:-1]))

comprehension = ('[' + operation + ']').setParseAction(lambda ts: Comprehension(ts[1]))

operation << (comma | projection | comprehension | chain)

piped = delimitedList(operation, '|').setParseAction(lambda ts: Sequence(ts.asList()))

