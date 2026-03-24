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

def reshape_and_transform() -> dict[str, np.ndarray]:
    """
    Perform reshape and transpose operations.

    Returns:
        dict: Transformed arrays
    """
    arr: np.ndarray = np.arange(12)
    matrix: np.ndarray = arr.reshape(3, 4)

    return {
        "matrix": matrix,
        "transpose": matrix.T,
        "flatten": matrix.flatten(),
    }


def concatenate_and_split() -> dict[str, list[np.ndarray] | np.ndarray]:
    """
    Concatenate and split arrays.

    Returns:
        dict: Results of operations
    """
    a: np.ndarray = np.array([1, 2, 3])
    b: np.ndarray = np.array([4, 5, 6])

    concatenated: np.ndarray = np.concatenate([a, b])
    stacked: np.ndarray = np.vstack([a, b])
    split_arrays: list[np.ndarray] = np.split(concatenated, 2)

    return {
        "concatenated": concatenated,
        "stacked": stacked,
        "split": split_arrays,
    }

def main() -> None:
    """
    Main function to demonstrate array transformations.

    Returns:
        None
    """
    print_string("Reshape and Transform")
    reshape_results = reshape_and_transform()
    for key, value in reshape_results.items():
        print(f"{key} : \n")
        array_infos(value)

    print_string("Concatenate and Split")
    concat_results = concatenate_and_split()
    for key, value in concat_results.items():
        print(f"{key}: \n")
        if isinstance(value, list):
            for i, arr in enumerate(value):
                print(f"Part {i}:\n")
                array_infos(arr)
        else:
            array_infos(value)
if __name__ == "__main__":
    main()
