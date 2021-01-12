import unittest
from PRNParser import PRNParser, ParseStatus


class PRNParserTest(unittest.TestCase):
    # def __init__(self, *args, **kwargs):
    #     super(PRNParsetTest, self).__init__(*args, **kwargs)

    def ParseLine_TooLong_ExpectedError(self):
        test = PRNParser()
        res = test.ParseLine(
            'Hawksmoor                               Ackroyd,Peter                 978014017113644444444444444')
        print('EDLAR')
        self.assertEqual(ParseStatus('Error'), res)

    def ParseLine_TooShort_ExpectedIncomplete(self):
        test = PRNParser()
        res = test.ParseLine('Hawksmoor                               Ackroyd,Peter                 9784')
        self.assertEqual(ParseStatus('Incomplete'), res)

    def ParseLine_OK_ExpectedDone(self):
        test = PRNParser()
        res = test.ParseLine('Hawksmoor                               Ackroyd,Peter                 9780140171136')
        self.assertEqual(ParseStatus('Done'), res)

if __name__ == '__main__':
    unittest.main()

