#!/usr/bin/env python
import struct
import sys
from collections import Counter


def main():
    # Initialize
    argvs   = sys.argv
    data    = open(argvs[1], 'rb').read()
    buf     = []
    percent = []

    # make a list
    for i in data:
        buf.append(hex(ord(i)))

    counter = Counter(buf)
    total   = sum(counter.values())

    for w, c in counter.most_common():
        percent.append( [w, (float(c)/float(total)) * 100] )

    print "total:", sum(counter.values())
    print percent


if __name__ == '__main__':
    main()
