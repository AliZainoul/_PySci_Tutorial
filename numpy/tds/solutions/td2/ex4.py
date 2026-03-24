import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def array_infos(arr: np.ndarray) -> None:
    print("Array Infos ")
    print("Array: \n", arr)
    print("Shape:", arr.shape)
    print()


def filtering(values: np.ndarray) -> dict[str, np.ndarray]:
    """
    Apply advanced filtering.

    Args:
        values (np.ndarray): Input array.

    Returns:
        dict[str, np.ndarray]
    """
    return {
        "where": np.where(values < 0, 0, values),
        "mask": values[values > 0],
    }


def main() -> None:
    """
    Filtering demonstration.
    """
    print_string("Filtering")

    data: np.ndarray = np.random.randn(10)

    for name, result in filtering(data).items():
        print(name)
        array_infos(result)


if __name__ == "__main__":
    main()