import numpy as np
from scipy import integrate


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


def simple_integrals() -> dict[str, float]:
    """
    Compute simple integrals.

    Returns
    -------
    dict[str, float]
    """
    f = lambda x: x**2

    result_1, _ = integrate.quad(f, 0, 1)
    result_2, _ = integrate.quad(np.sin, 0, np.pi)
    result_3, _ = integrate.quad(np.cos, 0, 2 * np.pi)

    return {
        "x^2 (0,1)": result_1,
        "sin (0,pi)": result_2,
        "cos (0,2pi)": result_3,
    }


def double_integral() -> float:
    """
    Compute a double integral.

    Returns:
        float
    """
    f = lambda y, x: x * y

    result, _ = integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: 1)

    return result


def main() -> None:
    print_string("Integration")

    for name, value in simple_integrals().items():
        print(name, "=", value)

    print("\nDouble integral =", double_integral())


if __name__ == "__main__":
    main()
