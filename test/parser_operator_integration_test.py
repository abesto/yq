from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence
from yq.operators.subscript import Subscript
from yq.parser import parse


class ParserOperatorIntegrationTestCase(TestCase):
    def test_parse_empty_dot(self):
        data = {'foo': 3, 'bar': 'baz'}
        self.assertDictEqual(
            parse('.').apply(data),
            data
        )

    def test_dots(self):
        self.assertEqual(
            parse('.foo.bar').apply({'foo': {'bar': 42}}),
            42
        )

    def test_subscript(self):
        self.assertEqual(
            parse('[3]').apply([3,4,5,6]),
            6
        )

    def test_projection(self):
        self.assertDictEqual(
            parse('{foo,   boo}').apply({'foo': 3, 'boo': 30, 'bar': 'baz', 'baz': 'bar'}),
            {'foo': 3, 'boo': 30}
        )

    def test_piped(self):
        self.assertDictEqual(
            parse('[1] | {foo}').apply([3, {'foo': 4, 'bar': 'baz'}]),
            {'foo': 4}
        )
