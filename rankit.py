# TODO: The rank mechanism


class Domain:
    def __init__(self, path):
        self.path = path
        self.rank = 0
        self.sub = []

    def __str__(self):
        pass

    def add_sub(self, sub_domain):
        self.sub.append(sub_domain)


def path_parse(path_str):
    path_str.split('/')


def new_domain(path):
    path_parse()


if __name__ == '__main__':
    domain = Domain()