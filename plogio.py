import time

from config import PLOG_PATH, TESTCASE_PATH
from plogclass import PLog, StLog, RpLog, CdLog, PLogDate
from errors import PLogTypeError


class PLogReader:
    logs = []
    logs_parsed = []

    def __init__(self):
        self.logs = []

    def blank_filter(self):
        self.logs = [log.strip() for log in self.logs]

    def comment_filter(self):
        inline_comment_pattern = ''
        pass

    def preprocessor(self):
        self.blank_filter()
        self.comment_filter()

    def parse(self):
        self.logs_parsed = []
        for log in self.logs:
            params = {}
            words = log.split(' ')
            if words[0] not in PLog.types:
                raise PLogTypeError

            log_type = words[0]
            for i in range(1, len(words)//2+2, 2):
                params[words[i]] = words[i+1]
            new_log = (log_type, params)

            self.logs_parsed.append(new_log)

    def read(self, fp):
        with open(fp, 'r') as plog_text:
            self.logs = plog_text.readlines()

        self.preprocessor()
        self.parse()
        return self.log_logs()

    @staticmethod
    def logit(type, **params):
        log_map = {'st': StLog, 'rp': RpLog, 'cd': CdLog}
        return log_map[type](**params)

    def log_logs(self):
        new_plogs = []
        for log_parsed in self.logs_parsed:
            log_type, params = log_parsed
            new_plog = self.logit(log_type, **params)
            new_plogs.append(new_plog)
        return new_plogs


class PLogLogger:
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
    """"
    plog_reader = PLogReader()
    plogs = plog_reader.read(TESTCASE_PATH+'test.plog')

    plog_date = PLogDate(plogs)
    print(plog_date)
    print(plog_date.count('cd'))
    """
    print(time.strftime("%a"))
