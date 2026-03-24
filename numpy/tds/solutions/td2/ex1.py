import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    """
    Print a given string.

    Args:
        s (str): The string to print.

    Returns:
        None
    """
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def array_infos(arr: np.ndarray) -> None:
    """
    Print information about a given NumPy array.

    Args:
        arr (np.ndarray): The input array to analyze.

    Returns:
        None
    """
    print("Array Infos ")
    print("Array: \n", arr)
    print("Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dtype:", arr.dtype)
    print()


def broadcasting_2d() -> dict[str, np.ndarray]:
    """
    Demonstrate 2D broadcasting.

    Returns
    -------
    dict[str, np.ndarray]
    """
    matrix: np.ndarray = np.arange(12).reshape(3, 4)
    vector: np.ndarray = np.array([1, 2, 3, 4])
    factors: np.ndarray = np.array([1, 2, 3])

    return {
        "add_vector": matrix + vector,
        "row_scaling": matrix * factors[:, np.newaxis],
    }

def main() -> None:
    """
    Broadcasting demonstration.

    Returns:
        None
    """
    print_string("Broadcasting")

    for name, result in broadcasting_2d().items():
        print(name)
        array_infos(result)


if __name__ == "__main__":
    main()
