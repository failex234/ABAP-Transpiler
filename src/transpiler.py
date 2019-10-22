import fparser
import misc as appmisc
import sys

# make sure this file is being run directly
if __name__ == '__main__':
    if len(sys.argv) == 1:
        appmisc.usage(sys.argv[0])
        exit(1)
    else:
        file = appmisc.file_open(sys.argv[1])
        if (file != None):
            appparser = fparser.Parser(file)
            appparser.parse()
            appmisc.file_close(file)
        else:
            appmisc.print_err("{}: no such file or directory".format(sys.argv[1]))
            exit(1)
        pass