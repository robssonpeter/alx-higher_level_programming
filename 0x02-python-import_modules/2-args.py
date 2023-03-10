#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")

    for n in range(1, len(sys.argv)):
        print(f"{n}: {sys.argv[n]}")
