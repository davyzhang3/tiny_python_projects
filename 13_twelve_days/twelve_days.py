#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-24
Purpose: Rock the Casbah
"""

import argparse, sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout
                        )

    args = parser.parse_args()

    if args.num not in range(1,13,1):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    verses = [verse(n) for n in range(1, args.num+1)]
    # verse = map(verse, range(1, args.num+1))
    print('\n\n'.join(verses), file=args.outfile)

def verse(day):
    """Create a verse"""
    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    gifts = [
    'A partridge in a pear tree.',
    'Two turtle doves,',
    'Three French hens,',
    'Four calling birds,',
    'Five gold rings,',
    'Six geese a laying,',
    'Seven swans a swimming,',
    'Eight maids a milking,',
    'Nine ladies dancing,',
    'Ten lords a leaping,',
    'Eleven pipers piping,',
    'Twelve drummers drumming,',
    ]

    a = [f'On the {ordinal[day-1]} day of Christmas,', 'My true love gave to me,']
    b = [gifts[n] for n in range(day-1,-1,-1)]
    a.extend(b)
    
    if day > 1:
        a[-1] = a[-1].replace('A', 'And a')

    return '\n'.join(a)

def test_verse():
    """Test verse"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,', 'A partridge in a pear tree.'
    ])
    assert verse(2) == '\n'.join(['On the second day of Christmas,', 'My true love gave to me,',
    'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
