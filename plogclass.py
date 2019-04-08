import re


class PLog:
    types = ['st', 'rp', 'cd']

    def __init__(self, type, **params):
        self.type = type
        self.params = params

    def __str__(self):
        params_repr = ' '.join([key + ' ' + self.params[key] for key in self.params])
        return self.type + ' ' + params_repr


class StLog(PLog):
    def __init__(self, **params):
        super().__init__('st', **params)


class RpLog(PLog):
    def __init__(self, **params):
        super().__init__('rp', **params)


class CdLog(PLog):
    def __init__(self, **params):
        super().__init__('cd', **params)


class PLogDate:
    def __init__(self, plogs):
        self.plogs = plogs

    def __str__(self):
        return ' '.join([str(plog) for plog in self.plogs])

    def __len__(self):
        return len(self.plogs)

    def count(self, log_type):
        return len([plog for plog in self.plogs if plog.type == log_type])

    def percentage(self, log_type):
        return self.count(log_type) / len(self)


if __name__ == '__main__':
    pass