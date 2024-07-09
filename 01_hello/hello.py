#!/usr/bin/env python3

#Say Hello! 

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n','--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()

def main():
   
    args = get_args()
    name = args.name
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':  #dunder name == dunger main
    main()