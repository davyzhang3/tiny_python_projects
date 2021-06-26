#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-25
Purpose: Rock the Casbah
"""

import argparse
import re, sys, os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    # words = [word for line in text.splitlines() for word in line.split()]

    # print(' '.join(map(word2num, words)))
    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))

def word2num(word):
    """convert word to it's number"""

    word = re.sub('[^a-zA-Z0-9]', '', word)

    return str(sum(map(ord, word)))

def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"

# --------------------------------------------------
if __name__ == '__main__':
    main()
