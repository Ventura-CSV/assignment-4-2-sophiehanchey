import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'a\nf'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    regex_string = r'[\w,\W]*a'
    regex_string += r'[\w,\W]*b'
    regex_string += r'[\w,\W]*c'
    regex_string += r'[\w,\W]*d'
    regex_string += r'[\w,\W]*e'
    regex_string += r'[\w,\W]*f'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'f\na\na\nf'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    regex_string = r'[\w,\W]*a'
    regex_string += r'[\w,\W]*b'
    regex_string += r'[\w,\W]*c'
    regex_string += r'[\w,\W]*d'
    regex_string += r'[\w,\W]*e'
    regex_string += r'[\w,\W]*f'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n2\no\ns'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    regex_string = r'[\w,\W]*o'
    regex_string += r'[\w,\W]*p'
    regex_string += r'[\w,\W]*q'
    regex_string += r'[\w,\W]*r'
    regex_string += r'[\w,\W]*s'
    regex_string += r'[\w,\W]*'
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())
