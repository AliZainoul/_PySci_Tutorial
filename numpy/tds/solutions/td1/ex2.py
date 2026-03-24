import numpy as np

def print_string(s: str = '', sep : str = "=") -> None:
    """
    Print a given string.

    Args:
        s (str): The string to print.

    Returns:
        None
    """
    print('\n' +sep * 31 + " " + s  + " " + sep * 31 + '\n')

def array_infos(arr : np.ndarray) -> None:
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


def array_slicing() -> dict[str, np.ndarray]:
    """
    Perform slicing operations on a 1D array.

    Returns:
        dict: Various sliced arrays
    """
    arr: np.ndarray = np.arange(20)

    return {
        "sub_array": arr[5:16],
        "every_second": arr[::2],
        "reversed": arr[::-1],
    }


def matrix_slicing() -> dict[str, np.ndarray]:
    """
    Perform slicing operations on a 2D matrix.

    Returns:
        dict: Extracted parts of the matrix
    """
    matrix: np.ndarray = np.arange(1, 17).reshape(4, 4)

    return {
        "row": matrix[1, :],
        "column": matrix[:, 2],
        "center": matrix[1:3, 1:3],
    }

def main() -> None:
    """
    Main function to demonstrate array and matrix slicing.

    Returns:
        None
    """
    print_string("Array Slicing")

    print_string("Original array", sep = "-")
    array_infos(np.arange(20))

    print_string("Sliced parts", sep = "-")
    for name, sliced in array_slicing().items():
        print(f"{name}:\n")
        array_infos(sliced)

    print_string("Matrix Slicing")

    print_string("Original matrix", sep = "-")
    array_infos(np.arange(1, 17).reshape(4, 4))

    print_string("Sliced parts", sep = "-")
    for name, sliced in matrix_slicing().items():
        print(f"{name}:\n")
        array_infos(sliced)


if __name__ == "__main__":
    main()
