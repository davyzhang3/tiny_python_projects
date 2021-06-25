#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-24
Purpose: Rock the Casbah
"""

import argparse
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    cluster = 'bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr'.split()
    prefixes = list(c for c in string.ascii_lowercase if c not in 'aeiou') + cluster

    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of  word"""
   
    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    word = word.lower()
    match = re.match(f'([{consonants}]+)?([aeiou])(.*)', word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word, '')

def test_stemmer():
    """test stemmer """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
