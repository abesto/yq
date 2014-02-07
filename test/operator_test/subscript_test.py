from unittest import TestCase
from yq.operators.match_error import MatchError
from yq.operators.subscript import Subscript


class SubscriptTestCase(TestCase):
    def test_simple(self):
        self.assertEqual(
            Subscript(1).apply(['foo', 'bar', 'baz']),
            'bar'
        )

    def test_repr(self):
        self.assertEqual(
            repr(Subscript(12)),
            '[12]'
        )

    def test_index_out_of_range(self):
        with self.assertRaises(MatchError):
            Subscript(1).apply([])
