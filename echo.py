#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    # parser.add_argument('-h', '--help', help='prints this message')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase', default=False)
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase', default=False)
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase', default=False)
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""
    result = args.text

    if args.upper:
        result = args.text.upper()

    if args.lower:
        result = args.text.lower()

    if args.title:
        result = args.text.title()

    return result


if __name__ == '__main__':
    print(main(create_parser().parse_args()))
