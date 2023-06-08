#!/usr/bin/python3

def main():
    import sys

    size = len(sys.argv) - 1
    result = 0

    if size == 0:
        print("0")
    else:
        for i in range(1, size + 1):
            result += int(sys.argv[i])

        print(result)


if __name__ == "__main__":
    main()
