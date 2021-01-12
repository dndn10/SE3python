class ParseStatus:
    def __init__(self, status) -> None:
        self.status = status

    def get_status(self):
        return self.status


class Book:
    title = None
    author = None
    isbn = None


class PRNParser:
    def ParseLine(self, line: str) -> str:
        """
        docstring
        """
        if len(line) < 83:
            return ParseStatus('Incomplete')
        elif len(line) > 83:
            return ParseStatus('Error')
        self.tmp = Book
        self.tmp.title = line[0:39]
        self.tmp.author = line[40:69]
        self.tmp.isbn = line[70:]

        return ParseStatus('Done')

    def GetLastRead(self):
        return self.tmp if self.tmp else 'No line read'
