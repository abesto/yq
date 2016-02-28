import yaml
import json
import cli


def jq_test():
    i = 0
    skipped = []
    lines = []
    for line in open('functional_tests/jq.txt', 'r'):
        line = line.strip()
        if not line:
            if lines:
                if lines[0] == 'skip':
                    skipped.append('\n'.join(lines[1:]))
                else:
                    yield (FunctionalTestCase('jq.txt', i,
                                              {'filter': lines[0],
                                               'input': json.loads(lines[1]),
                                               'output_list': lines[2:]}),)
                lines = []
                i += 1
        elif line[0] != '#':
            lines.append(line)


class FunctionalTestCase(object):
    def __init__(self, file, idx, case):
        self.case = case
        self.description = '%s case %d: %s' % (file, idx, case)

    def __call__(self):
        output = cli.main(self.case['filter'], yaml.dump(self.case['input']))
        if 'output' in self.case:
            expected_list = [self.case['output']]
        else:
            expected_list = self.case['output_list']
        for expected in expected_list:
            actual = output.next()
            print 'Actual: %s\nExpected: %s' % (actual, expected)
            expected = yaml.load(expected)
            assert actual == expected

