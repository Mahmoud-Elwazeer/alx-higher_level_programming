#!/usr/bin/python3

def main():
    import hidden_4

    argv = dir(hidden_4)

    for i in argv:
        if i[0] != '_':
            print(i)


if __name__ == "__main__":
    main()
