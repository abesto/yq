from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence
from yq.operators.subscript import Subscript
from yq.parser import parse


class ParserOperatorIntegrationTestCase(TestCase):
    def test_parse_empty_dot(self):
        data = {'foo': 3, 'bar': 'baz'}
        self.assertDictEqual(
            parse('.')._apply_item(data),
            data
        )

    def test_dots(self):
        self.assertEqual(
            parse('.foo.bar')._apply_item({'foo': {'bar': 42}}),
            42
        )

    def test_subscript(self):
        self.assertEqual(
            parse('[3]')._apply_item([3,4,5,6]),
            6
        )

    def test_projection(self):
        self.assertDictEqual(
            parse('{foo,   boo}')._apply_item({'foo': 3, 'boo': 30, 'bar': 'baz', 'baz': 'bar'}),
            {'foo': 3, 'boo': 30}
        )

    def test_piped(self):
        self.assertDictEqual(
            parse('[1] | {foo}')._apply_item([3, {'foo': 4, 'bar': 'baz'}]),
            {'foo': 4}
        )
