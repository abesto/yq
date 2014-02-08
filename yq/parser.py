from pyparsing import *
import yaml
from yq.operators.comma import Comma
from yq.operators.comprehension import Comprehension
from yq.operators.constant import Constant
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

# Literal values
literals = oneOf('true false null') | ('"'+Word(alphanums)+'"') | (Word(nums + '- .')).setName('literal')
literals.setParseAction(lambda ts: Constant(yaml.load(ts[0])))

# Operations
operation = Forward()

emptyDot = Literal('.').setParseAction(lambda ts: Dot())
dot = (('.' + key()).setName('dot_str') |
       ('.["' + key() + '"]').setName('dot_subscript_str') |
       ('."' + key() + '"').setName('dot_quote_str')).setParseAction(lambda ts: Dot(ts[1]))

extract = (Literal('.[]').setParseAction(Extract).setName('extract') |
           (dot + '[]').setParseAction(lambda ts: Sequence([ts[0], Extract()])))

subscript = ('[' + delimitedList(Word(nums)) + ']')\
    .setParseAction(lambda ts: Subscript(map(int, ts[1:-1])))\
    .setName('subscript')

subsequence = ('[' + Optional(Word(nums + '-'), None) + ':' + Optional(Word(nums + '-'), None) + ']')\
    .setParseAction(lambda ts: Subsequence(ts[1], ts[3]))\
    .setName('subsequence')

chainable = extract | dot | emptyDot | subscript | subsequence | literals
chain = OneOrMore(chainable).setParseAction(lambda ts: Sequence(ts.asList())).setName('chain')

comma = delimitedList(chain).setParseAction(Comma)

projectionItem = (
    (key() + ':' + chain).setParseAction(lambda ts: ProjectionItem(ts[0], ts[2])) |
    key().setParseAction(lambda ts: ProjectionItem(ts[0], Dot(ts[0])))
).setName('projection_item')
projection = ('{' + Optional(delimitedList(projectionItem, ',')) + '}').setParseAction(lambda ts: Projection(ts[1:-1])).setName('projection')

comprehension = ('[' + operation + ']').setParseAction(lambda ts: Comprehension(ts[1]))

operation << (comma | projection | comprehension | chain)

piped = delimitedList(operation, '|').setParseAction(lambda ts: Sequence(ts.asList()))

