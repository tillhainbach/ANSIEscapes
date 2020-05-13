import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pyansiescapes.enums import Colors

def make_8bit_color_function():
    for name in list(Colors.__members__.keys()) [:-1]:
        # ignore the last value "_blink" which is for internal use
        args = ("\n\tdrawing_level: t.DrawingLevelArg"
                "= ColorDrawingLevel.foreground")
        ret = 'color8("{}, drawing_level")'.format(name)
        docs = ('\t\"\"\"Convenience function for 8-bit {} color.\n'
                '\t\n'
                '\tSee :func:`color_8bit` for further details.\n'
                '\t\"\"\"'.format(name))
        make_function_skeleton(name.lower(), args, docs, ret)

def make_function_skeleton(funcName, args, docs, ret) -> None:
    print('def {}({}) -> str:'.format(funcName, args))
    print(docs)
    print('\treturn {}\n'.format(ret))

def make_text_formatting_function() -> None:
    for textAttribute in list(TextAttributes.__members__.keys()):
        ret = '_format_rich_text(TextAttributes.{})'.format(textAttribute)
        make_function_skeleton(textAttribute, "", ret)


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
