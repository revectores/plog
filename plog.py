import sys, time
import plogclass, plogio

# TODO: Interface to the cli


def get_context():
    context = []
    timestamp = ['-_timestamp', str(time.time())]
    context += timestamp
    return context


if __name__ == '__main__':
    print(time.time())
    text2plog = plogio.PLogProcessor()
    plog_file = plogio.PlogFile()

    context = get_context()
    plog = ' '.join(sys.argv[1:] + context)
    print(plog)
    print(text2plog.parse(plog))
    plog_file.read()
