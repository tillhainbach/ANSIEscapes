import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ansiEscapesEnums import *

def make8bitColorFunction():
    for name in list(Colors.__members__.keys()) [:-1]:
        # ignore the last value "_blink" which is for internal use
        args = "drawingLevel = ColorDrawingLevel.foreground"
        ret = 'color8("{}")'.format(name)
        makeBasicFunctionSkeleton(name.lower(), args, ret)

def makeBasicFunctionSkeleton(funcName, args, ret):
    print('@staticmethod')
    print('def {}({}):'.format(funcName, args))
    print('\treturn {}\n'.format(ret))

def makeTextFormattingFunction():
    for textAttribute in list(TextAttributes.__members__.keys()):
        ret = '_formatRichText(TextAttributes.{})'.format(textAttribute)
        makeBasicFunctionSkeleton(textAttribute, "", ret)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        def getFuncs():
            for key, value in globals().items():
                if callable(value) and value.__module__ == __name__:
                    yield key
        funcs = list(getFuncs()) [:-1]
        print('please provide function to run')
        print('Choises are:\n\t{}'.format('\n\t'.join(funcs)))
        sys.exit(0)

    else:
        for func in sys.argv[1:]:
            globals()[func]()
