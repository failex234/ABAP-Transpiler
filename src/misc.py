import sys
import re

"""
print program usage
"""
def usage(prgname):
    print("usage: {} [FILE]".format(prgname))

"""
safe file opening
"""
def file_open(filename):
    tempfile = None
    try:
        tempfile = open(filename, "r", encoding='utf-8')
    except:
        pass

    return tempfile

"""

"""
def file_close(file):
    file.close()

"""
print messages to stderr
"""
def print_err(*args, **kargs):
    print(*args, file=sys.stderr, **kargs)

"""
determine the instruction type of a line
"""
def get_line_type(line):
    if (re.match("\\s{0,}(let|var)\\s.+\\s{0,}=\\s{0,}.+;\\s{0,2}", line) != None):
        return 'VAR_DECLARATION_SET'
    elif (re.match("^\\/\\/.{0,}", line) != None):
        return 'COMMENT_SINGLELINE'
    return 'UNKNOWN'

"""
currently extremly naive method. JUST FOR TESTING!
"""
def get_var_contents(line):
    return line.split(' ')[4]

"""
custom split function to ignore spaces in quotes
"""
def split(line):
    # ignore spaces in strings
    pass