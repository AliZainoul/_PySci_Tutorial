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
    
def simple_filter(values: np.ndarray) -> dict[str, np.ndarray | int]:
    """
    Filter values using a boolean mask.

    Args:
        values: Input array

    Returns:
        dict: Filtered values and count
    """
    mask: np.ndarray = values > 50

    return {
        "filtered": values[mask],
        "count": int(np.sum(mask)),
    }


def advanced_filter(values: np.ndarray) -> np.ndarray:
    """
    Replace values outside a range with the mean.

    Args:
        values: Input array

    Returns:
        np.ndarray: Modified array
    """
    mask: np.ndarray = (values >= -1) & (values <= 1)
    mean_value: float = float(np.mean(values))

    result: np.ndarray = values.copy()
    result[~mask] = mean_value

    return result

def main() -> None:
    """
    Main function to demonstrate filtering operations.

    Returns:
        None
    """
    arr: np.ndarray = np.random.uniform(-100, 100, size=100)

    print_string("Simple Filter")
    simple_result = simple_filter(arr)
    print("Filtered Values:\n", simple_result["filtered"])
    print("Count:", simple_result["count"])

    print_string("Advanced Filter")
    advanced_result = advanced_filter(arr)
    print("Modified Array:\n", advanced_result)

if __name__ == "__main__":
    main()
