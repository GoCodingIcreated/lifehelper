from datetime import datetime


class Record:
    def __init__(self, text):
        self.creating_time = datetime.now()
        self.text = text

    def __str__(self):
        return str(self.creating_time.strftime("[%d.%m.%Y %H:%M]")) + ': ' + str(self.text)


class Subject(list):
    def __init__(self, name="unknown name"):
        list.__init__(self)
        self.name = name

    def __repr__(self):
        string = ['{']
        for rec in self:
            string.append('"' + str(rec) + '"')
            string.append(', ')
        string.pop()
        string.append('}')
        return ''.join(string)