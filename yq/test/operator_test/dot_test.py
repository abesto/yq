from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError


class DotTest(TestCase):
    data = {'foo': 'bar'}

    def test_simple(self):
        dot = Dot('foo')
        self.assertEqual(dot._apply_item(self.data), 'bar')

    def test_repr(self):
        self.assertEqual(repr(Dot('foo')), '.foo')

    def test_empty_key(self):
        self.assertEqual(Dot('')._apply_item(self.data), self.data)
        self.assertEqual(Dot()._apply_item(self.data), self.data)

    def test_no_such_key(self):
        dot = Dot('gah')
        self.assertIsNone(dot._apply_item({'bar': 3}))

    def test_not_an_object(self):
        dot = Dot('bah')
        with self.assertRaises(MatchError) as cm:
            dot._apply_item([1,2,3])
        self.assertEqual(cm.exception.error, 'tried to access field .bah on a non-object')

    def test_not_an_object_empty_dot(self):
        l = [1]
        self.assertListEqual(Dot().apply(l), l)