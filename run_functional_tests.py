import glob
import yaml
import cli


def functional_test():
    for file in glob.glob('functional_tests/*.yml'):
        with open(file, 'r') as fd:
            suite = yaml.load(fd.read())
        for idx, case in enumerate(suite):
            if 'skip' in case and case['skip']:
                continue
            yield (FunctionalTestCase(file, idx, case),)


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
            assert actual == expected

