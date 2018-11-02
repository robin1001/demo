import sys
import struct
import re
import argparse

FLAGS = None


if __name__ == '__main__':
    usage = '''Usage: demo usage'''
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('--flag', action='store_true',
                        help='demo flag')
    parser.add_argument('--port', type=int, default=10086,
                        help='demo port')
    parser.add_argument('--string',
                        help='demo string')
    parser.add_argument('position',
                        help='demo position')                        
    FLAGS = parser.parse_args()
