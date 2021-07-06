#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv)
    if arg_num == 1:
        print("{:d} argument.".format(arg_num - 1))
    elif arg_num == 2:
        print("{:d} argument:".format(arg_num - 1))
    else:
        print("{:d} arguments:".format(arg_num - 1))
    for i in range(arg_num):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
