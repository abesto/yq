from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence


class SequenceTestCase(TestCase):
    def test_dots(self):
        data = {'a': {'b': 'c'}}
        dot_a = Dot('a')
        dot_b = Dot('b')
        sequence = Sequence([dot_a, dot_b])
        self.assertEqual(sequence.apply([data]), ['c'])

    def test_dots_repr(self):
        sequence = Sequence([Dot('foo'), Dot('bar')])
        self.assertEqual(repr(sequence), '.foo.bar')