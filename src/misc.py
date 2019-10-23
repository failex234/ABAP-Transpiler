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
    if (re.match("^\\s{0,}(let|var)\\s+[^=\\s]+;\\s{0,}$", line) != None):
        return 'VAR_DECLARATION'
    elif (re.match("^\\s{0,}(let|var|const)\\s+.+\\s{0,}=\\s{0,}.+;\\s{0,2}", line) != None):
        return 'VAR_DECLARATION_SET'
    elif (re.match("^\\/\\/.{0,}", line) != None):
        return 'COMMENT_SINGLELINE'
    elif (re.match("^\\s{0,}.+\\..+\\(.{0,}\\);\\s{0,}", line) != None):
        # We can't determine if we wanted to call an instance or static method (ABAP uses different syntax for both)
        return 'CLASS_FUNCTION_CALL'
    elif (re.match("^\\s{0,}.+\\(.{0,}\\);\\s{0,}", line) != None):
        return 'FUNCTION_CALL'
    elif (re.match("^\\s{0,}(\\{|\\})\\s{0,}", line) != None):
        return 'BRACKET_ISOLATED'
    elif (re.match("^\\s{0,}function\\s+.+\\(.{0,}\\)\\s{0,}", line) != None):
        return 'FUNCTION_DEFINITION'
    elif (re.match("^\\s{0,}if\\s{0,}\\(.+\\)", line) != None):
        return 'IF_STATEMENT'
    elif (re.match("^.{0,}else.{0,}", line) != None):
        return 'ELSE_STATEMENT'
    elif (re.match("^\\s{0,}.{0,}else\\s+if\\s{0,}\\(.+\\)", line) != None):
        return 'IF_ELSE_STATEMENT'
    return 'UNKNOWN'

"""
get the contents of a defined variable from the definition line
"""
def get_var_contents(line):
    splitline = split(line)
    if (len(splitline) < 4):
        return None

    return splitline[3][:-1]

"""
custom split function to ignore spaces in quotes
"""
def split(line):
    # ignore spaces in strings
    quotesfound = ''
    spacespos = []
    spaces = []
    previousspace = 0

    # first find all the spaces that aren't inside any quotes
    for i in range(0, len(line)):
        if (quotesfound == '' and line[i] == ' '):
            spacespos.append(i)
        elif (quotesfound == '' and (line[i] == '"' or line[i] == "'")):
            quotesfound = line[i]
        elif (quotesfound == line[i]):
            quotesfound = ''

    # cut out the areas between the spaces
    for space in spacespos:
        if (previousspace != 0):
            spaces.append(line[previousspace + 1:space])
        else:
            spaces.append(line[:space])
        previousspace = space

    # when the string contains at least one space we still need to cut the last bit out
    if (len(spaces) > 0):
        spaces.append(line[previousspace + 1:])

    return spaces