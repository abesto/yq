from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError
from yq.operators.projection import Projection, ProjectionItem


class ProjectionTestCase(TestCase):
    def simple_test(self):
        p = Projection([ProjectionItem('foo', Dot('foo')), ProjectionItem('blam', Dot('blam'))])
        data = {'foo': 'bar', 'baz': 3, 'blam': 30}
        self.assertDictEqual(p._apply_item(data), {'foo': 'bar', 'blam': 30})

    def test_simple_repr(self):
        p = Projection([ProjectionItem('foo', Dot('foo')), ProjectionItem('blam', Dot('blam'))])
        self.assertEqual(
            repr(p),
            '{foo, blam}'
        )

    def test_other_dot_repr(self):
        self.assertEqual(
            repr(Projection([ProjectionItem('foo', Dot('bar'))])),
            '{foo: .bar}'
        )

