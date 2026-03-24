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

def vector_operations() -> dict[str, np.ndarray]:
    """
    Perform basic vectorized operations.

    Returns
    -------
    dict[str, np.ndarray]
    """
    a: np.ndarray = np.array([1, 2, 3, 4, 5])
    b: np.ndarray = np.array([10, 20, 30, 40, 50])

    return {
        "add": a + b,
        "multiply": a * b,
        "square": a ** 2,
        "sqrt": np.sqrt(b),
    }

def broadcasting_example() -> dict[str, np.ndarray]:
    """
    Demonstrate broadcasting operations.

    Returns
    -------
    dict[str, np.ndarray]
    """
    matrix: np.ndarray = np.arange(12).reshape(3, 4)

    normalized: np.ndarray = (matrix - matrix.mean(axis=0)) / matrix.std(axis=0)

    return {
        "add_scalar": matrix + 10,
        "row_scaling": matrix * np.array([1, 2, 3]).reshape(3, 1),
        "normalized": normalized,
    }

def main() -> None:
    """
    Main function to execute the NumPy basics demonstration.

    Returns:
        None
    """

    print_string("Vector Operations")
    for name, result in vector_operations().items():
        print(f"{name}:\n")
        array_infos(result)

    print_string("Broadcasting Example")
    for name, result in broadcasting_example().items():
        print(f"{name}:\n")
        array_infos(result)

if __name__ == "__main__":
    main()
