#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-23
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        nargs='+',
                        metavar='letter',
                        type=str,
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='File',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()

    # lookup = {line[0].upper(): line.rstrip() for line in fh} # dictionary comprehension
    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
