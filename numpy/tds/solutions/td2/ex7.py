import numpy as np
import timeit


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
    print("Array: \n", arr[:10])
    print("Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dtype:", arr.dtype)
    print()


# ==========================================================
# Core functions (loop vs vectorized)
# ==========================================================

def square_loop(arr: np.ndarray) -> np.ndarray:
    """
    Compute square using Python loop.

    Args:
        arr (np.ndarray): Input array.

    Returns:
        np.ndarray
    """
    result: np.ndarray = np.zeros_like(arr)

    for i in range(arr.size):
        result[i] = arr[i] ** 2

    return result


def square_vectorized(arr: np.ndarray) -> np.ndarray:
    """
    Compute square using NumPy vectorization.

    Args:
        arr (np.ndarray): Input array.

    Returns:
        np.ndarray
    """
    return arr ** 2


# ==========================================================
# Benchmark
# ==========================================================

def benchmark(n: int, repeat: int = 5) -> dict[str, float]:
    """
    Benchmark loop vs vectorized approach.

    Args:
        n (int): Array size.
        repeat (int): Number of repetitions.

    Returns:
        dict[str, float]
    """
    arr: np.ndarray = np.arange(n)

    loop_time: float = timeit.timeit(
        lambda: square_loop(arr),
        number=repeat
    )

    vector_time: float = timeit.timeit(
        lambda: square_vectorized(arr),
        number=repeat
    )

    return {
        "size": n,
        "loop_time": loop_time,
        "vectorized_time": vector_time,
        "speedup": loop_time / vector_time if vector_time > 0 else float("inf"),
    }


# ==========================================================
# MAIN
# ==========================================================

def main() -> None:
    """
    Execute performance comparison.

    Returns:
        None
    """
    print_string("Performance Benchmark")

    sizes: list[int] = [10_000, 100_000, 1_000_000]

    for size in sizes:
        result = benchmark(size)

        print(f"Size: {result['size']}")
        print(f"Loop time: {result['loop_time']:.6f} s")
        print(f"Vectorized time: {result['vectorized_time']:.6f} s")
        print(f"Speedup: x{result['speedup']:.2f}")
        print("-" * 50)


if __name__ == "__main__":
    main()
