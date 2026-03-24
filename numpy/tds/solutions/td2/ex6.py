import numpy as np


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def save_load() -> dict[str, np.ndarray]:
    """
    Save and load array.

    Returns:
        dict[str, np.ndarray]
    """
    arr = np.arange(10)

    np.save("data.npy", arr)
    loaded = np.load("data.npy")

    return {"original": arr, "loaded": loaded}


def main() -> None:
    """
    Save/load demonstration.
    """
    
    print_string("Save/Load")

    for k, v in save_load().items():
        print(k, v)


if __name__ == "__main__":
    main()
