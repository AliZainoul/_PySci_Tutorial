import numpy as np
import scipy as sp
import scipy.integrate as integrate
import scipy.linalg as linalg
import scipy.fft as fft


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


# ==========================================================
# Core functions
# ==========================================================

def scipy_basics() -> dict[str, str]:
    """
    Display SciPy version and loaded modules.

    Returns
    -------
    dict[str, str]
    """
    return {
        "scipy_version": sp.__version__,
        "modules": f"{dir(integrate)=}, \n {dir(linalg)=}, \n {dir(fft)=} \n",
    }


def numpy_dependency_check() -> np.ndarray:
    """
    Create a simple NumPy array (SciPy dependency check).

    Returns:
        np.ndarray
    """
    return np.arange(10)


# ==========================================================
# MAIN
# ==========================================================

def main() -> None:
    """
    SciPy basics demonstration.

    Returns:
        None
    """
    print_string("SciPy Basics")

    info = scipy_basics()

    print("SciPy version:", info["scipy_version"])
    print("Loaded modules:", info["modules"])
    print()

    print_string("NumPy Dependency Check")
    arr = numpy_dependency_check()
    array_infos(arr)


if __name__ == "__main__":
    main()