import numpy as np
from scipy.interpolate import interp1d, CubicSpline


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def interpolation() -> dict[str, np.ndarray]:
    """
    Perform linear and cubic interpolation.

    Returns
    -------
    dict[str, np.ndarray]
    """
    x = np.linspace(0, 10, 5)
    y = np.sin(x)

    x_new = np.linspace(0, 10, 100)

    linear = interp1d(x, y)
    cubic = CubicSpline(x, y)

    return {
        "linear": linear(x_new),
        "cubic": cubic(x_new),
    }


def main() -> None:
    print_string("Interpolation")

    for k, v in interpolation().items():
        print(k)
        print(v[:10], "\n")


if __name__ == "__main__":
    main()
