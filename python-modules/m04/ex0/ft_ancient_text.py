#! /usr/bin/python3

import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        f: IO[str] | None = None
        try:
            f = open(file_name, "r")
            print("---")
            print(f.read())
            print("---")
        except OSError as e:
            print(f"Error opening file '{file_name}': {e}")
        finally:
            if f is not None:
                f.close()
                print(f"File '{file_name}' closed.")
