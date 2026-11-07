#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if (temp_int > 40):
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40°C)")
    if (temp_int < 0):
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    test_vals = ("25", "abc", "100", "-50")
    for val in test_vals:
        print(f"Input data is '{val}'")
        try:
            temp = input_temperature(val)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
