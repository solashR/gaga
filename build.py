#!/usr/bin/env python

import json
import time
import string
import random


def _write_test_num():
    rand_num = random.randint(1, 1024)
    test_name = ''.join(random.choice(string.ascii_lowercase) for _ in xrange(10))
    with open(test_name, 'w') as fh:
        fh.write(str(rand_num))

    return test_name


def main():
    tests_count = random.randint(1, 100)
    tests = [_write_test_num() for _ in xrange(tests_count)]

    time.sleep(60)  # sleep because it a very long build
    print json.dumps(tests)


if __name__ == '__main__':
    main()
