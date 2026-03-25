import numpy as np
from scipy import linalg


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


def solve_system() -> dict[str, np.ndarray]:
    """
    Solve linear system Ax = b.

    Returns
    -------
    dict[str, np.ndarray]
    """
    A = np.array([[3, 1, 2],
                  [1, 2, 0],
                  [0, 1, 1]])

    b = np.array([10, 5, 3])

    x = linalg.solve(A, b)

    return {
        "solution": x,
        "verification": A @ x,
    }


def matrix_properties() -> dict[str, np.ndarray | float]:
    """
    Compute determinant and inverse.

    Returns
    -------
    dict[str, np.ndarray | float]
    """
    A = np.array([[1., 2., 3.],
                  [0., 1., 4.],
                  [5., 6., 0.]])

    return {
        "det": float(linalg.det(A)),
        "inverse": linalg.inv(A),
        "identity": A @ linalg.inv(A),
    }


def eigen_analysis() -> dict[str, np.ndarray]:
    """
    Compute eigenvalues and eigenvectors.

    Returns
    -------
    dict[str, np.ndarray]
    """
    A = np.array([[2, 1],
                  [1, 2]])

    values, vectors = linalg.eig(A)

    return {
        "eigenvalues": values,
        "eigenvectors": vectors,
    }


def main() -> None:
    print_string("Linear Algebra")

    for k, v in solve_system().items():
        print(k)
        array_infos(v)

    for k, v in matrix_properties().items():
        print(k)
        if isinstance(v, np.ndarray):
            array_infos(v)
        else:
            print(v, "\n")


if __name__ == "__main__":
    main()
