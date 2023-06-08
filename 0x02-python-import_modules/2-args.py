#!/usr/bin/python3

def main():
    import sys

    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size))

    for i in range(1, size + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
