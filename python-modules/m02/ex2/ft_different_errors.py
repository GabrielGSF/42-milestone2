#! /usr/bin/python3

def garden_operations(operation_number: int) -> int | None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            100/0
        case 2:
            open("/non/existent/file")
        case 3:
            "ice" + 935
        case _:
            return operation_number
    return None


def test_error_types() -> None:
    test_vals = (0, 1, 2, 3, 4)
    for val in test_vals:
        print(f"Testing operation {val}...")
        try:
            garden_operations(val)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
