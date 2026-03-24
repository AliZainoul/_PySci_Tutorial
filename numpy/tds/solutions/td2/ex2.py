import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def array_infos(arr: np.ndarray) -> None:
    print("Array Infos ")
    print("Array: \n", arr)
    print("Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dtype:", arr.dtype)
    print()


def linear_algebra() -> dict[str, np.ndarray | float]:
    """
    Perform linear algebra operations.

    Returns
    -------
    dict[str, np.ndarray | float]
    """
    a: np.ndarray = np.arange(12).reshape(3, 4)
    b: np.ndarray = np.arange(8).reshape(4, 2)
    c: np.ndarray = np.array([[1., 2.], [3., 4.]])

    return {
        "matmul": a @ b,
        "determinant": float(np.linalg.det(c)),
        "inverse": np.linalg.inv(c),
    }

def main() -> None:
    """
    Linear algebra demonstration.

    Returns:
        None
    """
    print_string("Linear Algebra")

    results = linear_algebra()

    for name, result in results.items():
        print(name)
        if isinstance(result, np.ndarray):
            array_infos(result)
        else:
            print(result, "\n")


if __name__ == "__main__":
    main()