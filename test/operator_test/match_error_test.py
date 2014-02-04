from unittest import TestCase
from yq.operators.dot import Dot
from yq.operators.match_error import MatchError
import yaml


class MatchErrorTestCase(TestCase):
    def test_message(self):
        data = {'bar': ['baz']}
        exc = MatchError(Dot('foo'), data, 'error message')
        self.assertEqual('Failed to apply ".foo": error message. The data being processed was:\n%s' % yaml.dump(data),
                         exc.message)
