#! /usr/bin/python3

import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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

        print("Transform data:")
        new_lines: list[str] = []
        f_src: IO[str] | None = None
        read_ok = True
        try:
            f_src = open(file_name, "r")
            for line in f_src:
                new_lines.append(line.rstrip("\n") + "#\n")
            print("---")
            for line in new_lines:
                print(line, end="")
            print("---")
        except OSError as e:
            print(f"Error opening file '{file_name}': {e}")
            read_ok = False
        finally:
            if f_src is not None:
                f_src.close()

        if read_ok:
            new_file = input("Enter new file name (or empty): ")
            f_dst: IO[str] | None = None
            if new_file != "":
                try:
                    f_dst = open(new_file, "w")
                    print(f"Saving data to '{new_file}'")
                    for line in new_lines:
                        f_dst.write(line)
                    print(f"Data saved in file '{new_file}'.")
                except OSError as e:
                    print(f"Error opening file '{new_file}': {e}")
                finally:
                    if f_dst is not None:
                        f_dst.close()
            else:
                print("Not saving data.")
