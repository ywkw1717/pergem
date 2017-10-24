#!/usr/bin/env python
import struct
import sys
import numpy as np
import cv2
import math
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

    cols  = 16 * 8
    rows  = int(math.ceil(total / 128.0))
    image = np.zeros((rows, cols, 3), np.uint8)
    count = 0

    for i in range(rows):
        for j in range(cols):
            try:
                value = int(buf[count], 16)
            except:
                break
            if value == 0x00:
                b = 0
                g = 0
                r = 0
            elif value == 0xff:
                b = 255
                g = 255
                r = 255
            elif value > 0x00 and value < 0x20: # green
                b = 0
                g = 212 + (value - 0x01)
                r = 0
            elif value > 0x1f and value < 0x80: # red
                b = 0
                g = 0
                r = 128 + (value - 0x20)
            else: # blue
                b = 127 + (value - 0x80)
                g = 0
                r = 0

            count += 1
            for k in range(8):
                image.itemset((i, j, 0), b)
                image.itemset((i, j, 1), g)
                image.itemset((i, j, 2), r)

    cv2.imwrite("sample.png", image)


if __name__ == '__main__':
    main()
