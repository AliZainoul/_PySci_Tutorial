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

def descriptive_statistics(data: np.ndarray) -> dict[str, float]:
    """
    Compute descriptive statistics.

    Args:
        data: Input array

    Returns:
        dict: Statistical values
    """
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "variance": float(np.var(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "q25": float(np.percentile(data, 25)),
        "q75": float(np.percentile(data, 75)),
    }


def matrix_statistics(matrix: np.ndarray) -> dict[str, np.ndarray]:
    """
    Compute statistics on a matrix.

    Args:
        matrix: Input matrix

    Returns:
        dict: Computed statistics
    """
    return {
        "row_means": np.mean(matrix, axis=1),
        "col_sums": np.sum(matrix, axis=0),
        "argmax": np.argmax(matrix, axis=0),
    }

def main() -> None:
    """
    Main function to demonstrate descriptive statistics and matrix statistics.

    Returns:
        None
    """
    data: np.ndarray = np.random.rand(100)
    matrix: np.ndarray = np.random.rand(5, 5)

    print_string("Descriptive Statistics")
    array_infos(data)
    stats: dict[str, float] = descriptive_statistics(data)
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value:.4f}")

    print_string("Matrix Statistics")
    array_infos(matrix)
    matrix_stats: dict[str, np.ndarray] = matrix_statistics(matrix)
    for key, value in matrix_stats.items():
        print(f"{key.capitalize()}:\n{value}\n")

if __name__ == "__main__":
    main()
