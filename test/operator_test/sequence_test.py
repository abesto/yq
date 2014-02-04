from unittest import TestCase
from mock import sentinel
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence


class SequenceTestCase(TestCase):
    def test_dots(self):
        data = {sentinel.a: {sentinel.b: sentinel.value}}
        dot_a = Dot(sentinel.a)
        dot_b = Dot(sentinel.b)
        sequence = Sequence([dot_a, dot_b])
        self.assertEqual(sequence.apply(data), sentinel.value)

    def test_dots_repr(self):
        sequence = Sequence([Dot('foo'), Dot('bar')])
        self.assertEqual(repr(sequence), '.foo.bar')