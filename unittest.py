from config import TESTCASE_PATH


class UnitTest():
    pass


with open(TESTCASE_PATH+'test.plog', 'w') as test_plog:
    test_plog.write("st -m 'test' -t 10:00-11:00")