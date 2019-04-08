import time

from config import PLOG_PATH, PLOG_FILE, TESTCASE_PATH
from plogio import PLogProcessor, PLogDate


class PLogReader(PLogProcessor):
    def __init__(self):
        super().__init__()
        self.logs = []

    def read(self, fp):
        with open(fp, 'r') as plog_text:
            self.logs = plog_text.readlines()

        self.preprocessor()
        self.parse_logs(self.logs)
        return self.log_plogs()


class PLogLogger(PLogProcessor):
    def __init__(self, fp):
        self.fp = fp

    def new_doc(self):
        with open(self.fp) as f:
            div = "="*20
            today, weekday = time.strftime('%Y.%m.%d'), time.strftime('%a')
            f.write("// {div} {today} {weekday} {div}".format(div=div, today=today, weekday=weekday))

    def new_log(self):
        with open(self.fp) as f:
            t = time.strftime('%H:%M:%S')
            f.write("[{t}]".format(t=t))


if __name__ == '__main__':
    plog_reader = PLogReader()
    plogs = plog_reader.read(TESTCASE_PATH+'test.plog')

    plog_date = PLogDate(plogs)
    print(plog_date)
    print(plog_date.count('cd'))
