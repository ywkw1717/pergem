#!/usr/bin/env python
import struct
import sys
from collections import Counter
import numpy as np
import matploitlib.pyplot as plt


def main():
    # Initialize
    argvs   = sys.argv
    data    = open(argvs[1], 'rb').read()
    buf     = []
    percent = []
    x       = []
    y       = []

    # make a list
    for i in data:
        buf.append(hex(ord(i)))

    counter = Counter(buf)
    total   = sum(counter.values())

    for w, c in counter.most_common():
        x.append(w)
        y.append(int(c))
        percent.append( [w, (float(c)/float(total)) * 100] )

    print "total:", sum(counter.values())
    print percent

    plt.plot(np.array(x), np.array(y))
    plt.show()

if __name__ == '__main__':
    main()
