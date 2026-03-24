import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def structured_array() -> np.ndarray:
    """
    Create structured array.

    Returns:
        np.ndarray
    """
    dtype = np.dtype([
        ("name", "U10"),
        ("age", "i4"),
        ("grade", "f4"),
    ])

    data = np.array([
        ("Alice", 23, 15.5),
        ("Bob", 25, 12.0),
        ("Charlie", 22, 17.0),
    ], dtype=dtype)

    return np.sort(data, order="grade")


def main() -> None:
    """
    Structured arrays demonstration.
    """
    print_string("Structured Arrays")

    print(structured_array())


if __name__ == "__main__":
    main()
