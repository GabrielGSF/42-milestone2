#! /usr/bin/python3

import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.flush()
        sys.stderr.write("Usage: ft_stream_management.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        f: IO[str] | None = None
        read_ok = True
        try:
            f = open(file_name, "r")
            print("---")
            print(f.read())
            print("---")
        except OSError as e:
            sys.stdout.flush()
            sys.stderr.write(f"[STDERR] Error opening file '{file_name}': "
                             f"{e}\n")
            read_ok = False
        finally:
            if f is not None:
                f.close()
                print(f"File '{file_name}' closed.")

        if read_ok:
            new_lines: list[str] = []
            f_src: IO[str] | None = None
            try:
                print("Transform data:")
                f_src = open(file_name, "r")
                for line in f_src:
                    new_lines.append(line.rstrip("\n") + "#\n")
                print("---")
                for line in new_lines:
                    print(line, end="")
                print("---")
            except OSError as e:
                sys.stdout.flush()
                sys.stderr.write(f"[STDERR] Error opening file '{file_name}': "
                                 f"{e}\n")
                read_ok = False
            finally:
                if f_src is not None:
                    f_src.close()

            if read_ok:
                print("Enter new file name (or empty): ", end="")
                sys.stdout.flush()
                new_file = sys.stdin.readline()
                new_file = new_file.rstrip("\n")
                f_dst: IO[str] | None = None
                if new_file != "":
                    try:
                        print(f"Saving data to '{new_file}'")
                        f_dst = open(new_file, "w")
                        for line in new_lines:
                            f_dst.write(line)
                        print(f"Data saved in file '{new_file}'.")
                    except OSError as e:
                        sys.stdout.flush()
                        sys.stderr.write(f"[STDERR] Error opening file "
                                         f"'{new_file}': {e}\n")
                        print("Data not saved.")
                    finally:
                        if f_dst is not None:
                            f_dst.close()
                else:
                    print("Not saving data.")
