#!/usr/bin/env python3
"""
Author : Dawei Zhang <davyzhang325@gmail.com>
Date   : 2021-06-23
Purpose: Rock the Casbah
"""

import argparse
import os,random, string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations <0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    num_mutations = round(len(args.text) * args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    indexes = random.sample(range(len(args.text)), num_mutations)

    new_text = args.text

    for i in indexes:
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i + 1:]

    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
