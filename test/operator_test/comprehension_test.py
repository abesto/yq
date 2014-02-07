from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError
from yq.operators.comprehension import Comprehension


class SubscriptTestCase(TestCase):
    def test_simple(self):
        self.assertListEqual(
            Comprehension(Dot('foo'))._apply_item([{'foo': 3}, {'foo': 4, 'bar': 'baz'}]),
            [3, 4]
        )

    def test_repr(self):
        self.assertEqual(
            repr(Comprehension(Dot('bar'))),
            '[.bar]'
        )

    def test_not_a_list(self):
        with self.assertRaises(MatchError) as cm:
            Comprehension(None)._apply_item({1:2})
        self.assertEqual(cm.exception.error, 'tried to apply comprehension [None] to non-array')

