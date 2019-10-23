import misc
import re
class Parser:
    """The JavaScript Code Parser"""
    _filecontents = ''

    def __init__(self, file):
        tempfilecontents = ''
        for line in file:
            tempfilecontents = tempfilecontents + ' ' + line

        self._filecontents = tempfilecontents.split('\n')
        pass

    def parse(self):
        for line in self._filecontents:
            line = re.sub("^\s+", "", line)
            linetype = misc.get_line_type(line)
            # We should know what type of instruction we're dealing with so that we can translate it
            if (len(linetype) == 0):
                pass
            else:
                firsttype = linetype
                if (firsttype == 'VAR_DECLARATION_SET'):
                    print(misc.get_var_contents(line))
                    pass
        pass