from unittest import TestCase
from mock import patch

from yq.output import output


class OutputTest(TestCase):
    def test_output_string(self):
        self.assertEqual(output('foo'), 'foo')

    @patch('yq.output.yaml')
    def test_output_dict(self, mock_yaml):
        data = {'foo': 'bar'}
        self.assertEqual(output(data), mock_yaml.dump.return_value)
        mock_yaml.dump.assert_called_once_with(data)
