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

def estimate_pi(n_samples: int) -> float:
    """
    Estimate pi using Monte Carlo simulation.

    Parameters
    ----------
    n_samples : int

    Returns
    -------
    float
    """
    x: np.ndarray = np.random.rand(n_samples)
    y: np.ndarray = np.random.rand(n_samples)

    inside: np.ndarray = x**2 + y**2 <= 1
    return 4 * float(np.mean(inside))

def main() -> None:
    """
    Pi estimation demonstration.
    """
    print_string("Pi Estimation")

    n_samples: int = 1_000_000
    pi_estimate: float = estimate_pi(n_samples)
    print(f"Estimated Pi with {n_samples} samples: {pi_estimate}")

if __name__ == "__main__":
    main()
