import time
import pickle

from config import PLOG_PATH, PLOG_FILE, TESTCASE_PATH
from plogclass import PLog, StLog, RpLog, CdLog, PLogDate
from errors import PLogTypeError
from toolkit import get_pairs


class PlogFile:
    filename = PLOG_PATH + PLOG_FILE

    def write(self, plog):
        with open(self.filename, 'ab') as pf:
            bin1 = pickle.dumps(plog)
            pf.writelines([bin1])

    def read(self):
        with open(self.filename, 'rb') as pf:
            bin1 = pf.readline()
            record = pickle.loads(bin1)
            print(record)

    def search(self, **cond):
        pass


class PLogProcessor:
    logs = []
    logs_parsed = []

    def blank_filter(self):
        self.logs = [log.strip() for log in self.logs]

    def comment_filter(self):
        inline_comment_pattern = ''
        pass

    def preprocessor(self):
        self.blank_filter()
        self.comment_filter()

    def parse(self, log):
        params = {}
        words = log.split(' ')

        log_type = words[0]
        if log_type not in PLog.types:
            raise PLogTypeError

        params = get_pairs(words[1:])
        new_log = (log_type, params)
        return new_log

    def parse_logs(self, logs):
        self.logs_parsed = []
        for log in logs:
            new_log = self.parse(log)
            self.logs_parsed.append(new_log)

    @staticmethod
    def logit(type, **params):
        log_map = {'st': StLog, 'rp': RpLog, 'cd': CdLog}
        return log_map[type](**params)

    def log_plogs(self):
        new_plogs = []
        for log_parsed in self.logs_parsed:
            log_type, params = log_parsed
            new_plog = self.logit(log_type, **params)
            new_plogs.append(new_plog)
        return new_plogs

