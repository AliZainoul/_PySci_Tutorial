from typing import NamedTuple
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

def numpy_basics() -> None:
    """
    Demonstrate NumPy import, version, and basic array properties.

    Returns:
        None
    """
    arr: np.ndarray = np.arange(10)

    print_string("NumPy Basics")

    print("Version:", np.__version__)
    array_infos(arr)

class BasicMatrices(NamedTuple):
    """
    Container for basic NumPy matrices.
    """
    zeros: np.ndarray
    ones: np.ndarray
    identity: np.ndarray
    full: np.ndarray

def create_basic_matrices() -> BasicMatrices:
    """
    Create basic NumPy matrices.

    Returns:
        BasicMatrices: A named tuple containing the created matrices.
    """
    zeros_matrix: np.ndarray = np.zeros((3, 4))
    ones_matrix: np.ndarray = np.ones((4, 3))
    identity_matrix: np.ndarray = np.eye(5)
    full_matrix: np.ndarray = np.full((3, 3), 7)

    return BasicMatrices(zeros_matrix, ones_matrix, identity_matrix, full_matrix)

def main() -> None:
    """
    Main function to execute the NumPy basics and matrix creation.

    Returns:
        None
    """
    numpy_basics()
    matrices : BasicMatrices = create_basic_matrices()
    for matrix in matrices:
        array_infos(matrix)

if __name__ == "__main__":
    main()
