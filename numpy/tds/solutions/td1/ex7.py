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

def math_functions() -> dict[str, np.ndarray]:
    """
    Apply mathematical functions to an array.

    Returns:
        dict: Computed arrays
    """
    x: np.ndarray = np.linspace(0, 2 * np.pi, 10)

    return {
        "sin": np.sin(x),
        "cos": np.cos(x),
        "exp": np.exp(x),
        "log": np.log(x + 1),
        "rounded": np.round(np.sin(x), 2),
    }


def cumulative_operations(matrix: np.ndarray) -> dict[str, np.ndarray]:
    """
    Perform cumulative operations.

    Args:
        matrix: Input matrix

    Returns:
        dict: Results of cumulative operations
    """
    return {
        "cumsum": np.cumsum(matrix, axis=1),
        "cumprod": np.cumprod(matrix, axis=1),
        "row_sum": np.apply_along_axis(np.sum, 1, matrix),
    }

def main() -> None:
    """
    Main function to demonstrate the exercises.
    """
    arr: np.ndarray = np.random.rand(5, 5)

    math_results : dict[str, np.ndarray] = math_functions()
    print("Math Functions:")
    for key, value in math_results.items():
        print(f"{key}:\n")
        array_infos(value)

    cumulative_results : dict[str, np.ndarray]= cumulative_operations(arr)

    print("\nCumulative Operations:")
    for key, value in cumulative_results.items():
        print(f"{key}:\n")
        array_infos(value)
    
if __name__ == "__main__":
    main()
