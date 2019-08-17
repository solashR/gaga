#!/usr/bin/env python

import sys
import time
import argparse


def _parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('test_name')
    return parser.parse_args()


def main():
    args = _parse_cli()

    with open(args.test_name) as fh:
        num = int(fh.read())

    print num
    rc = 0
    if num % 27 == 0:
        rc = 7

    time.sleep(20)  # sleep because the test is very complicated
    return rc


if __name__ == '__main__':
    sys.exit(main())
