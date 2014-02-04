from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.sequence import Sequence
from yq.parser import parse


class ParserTestCase(TestCase):
    def test_parse_empty_dot(self):
        s = parse('.')
        self.assertIsInstance(s, Sequence)
        self.assertEqual(len(s.operators), 1)
        self.assertIsInstance(s.operators[0], Dot)
        self.assertEqual(s.operators[0].key, '')

    def test_dots(self):
        s = parse('.foo.bar')
        self.assertIsInstance(s, Sequence)
        self.assertEqual(s.operators[0].key, 'foo')
        self.assertEqual(s.operators[1].key, 'bar')
