#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        word = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, word))
        for i in range(1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))
