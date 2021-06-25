#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-25
Purpose: Rock the Casbah
"""
import re
import argparse
import os
import random
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble teh letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text of file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args





# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile(r"(\w(?:[a-zA-Z']*\w)?)")

    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))

def scramble(word):
    """scramble a word"""
    if len(word) < 4:
        return(word)
    else:
        middle = word[1:-1]
        middle = list(middle)
        random.shuffle(middle)
        return (word[0] + ''.join(middle) + word[-1])

def test_scramble():
    """test scrable"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == 'abc'
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()
