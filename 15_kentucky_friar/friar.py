#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-25
Purpose: Rock the Casbah
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input test or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words = re.split(r'(\W+)', args.text)
    print(''.join(map(fry, words)))

def fry(word):
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)

    if you:
        return you.group(1) + "'all"
    elif ing_word:
        first = ing_word.group(1)
        if re.search('[aeiouy]', first.lower()):
            return(first + "in'")
    return word
    

def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"

# --------------------------------------------------
if __name__ == '__main__':
    main()
