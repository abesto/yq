from unittest import TestCase
from mock import sentinel
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError


class DotTest(TestCase):
    data = {sentinel.key: sentinel.value}

    def test_simple(self):
        dot = Dot(sentinel.key)
        self.assertEqual(dot.apply(self.data), sentinel.value)

    def test_repr(self):
        self.assertEqual(repr(Dot('foo')), '.foo')

    def test_empty_key(self):
        self.assertEqual(Dot('').apply(self.data), self.data)
        self.assertEqual(Dot().apply(self.data), self.data)

    def test_no_such_key(self):
        dot = Dot('foo')
        with self.assertRaises(MatchError) as cm:
            dot.apply(self.data)
        self.assertIs(cm.exception.operator, dot)
        self.assertIs(cm.exception.data, self.data)
        self.assertEqual(cm.exception.error, 'key "foo" not found')
