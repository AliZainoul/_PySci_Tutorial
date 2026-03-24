import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def array_infos(arr: np.ndarray) -> None:
    print("Array Infos ")
    print("Array: \n", arr[:10])  # avoid huge print
    print("Shape:", arr.shape)
    print("Dtype:", arr.dtype)
    print()


def random_generation() -> dict[str, np.ndarray]:
    """
    Generate random distributions.

    Returns
    -------
    dict[str, np.ndarray]
    """
    np.random.seed(42)

    return {
        "normal": np.random.normal(0, 1, 1000),
        "uniform": np.random.uniform(0, 1, 1000),
        "exponential": np.random.exponential(1, 1000),
    }


def main() -> None:
    """
    Random generation demonstration.
    """
    print_string(" Random Generation")

    for name, result in random_generation().items():
        print(name)
        array_infos(result)


if __name__ == "__main__":
    main()
