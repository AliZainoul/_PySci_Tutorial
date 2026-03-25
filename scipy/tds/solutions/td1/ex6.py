import numpy as np
from scipy.optimize import curve_fit


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def linear_model(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return a * x + b


def curve_fitting() -> dict[str, float]:
    """
    Perform linear curve fitting.

    Returns
    -------
    dict[str, float]
    """
    x = np.linspace(0, 10, 50)
    y = 2 * x + 3 + np.random.normal(0, 1, size=x.shape)

    params, _ = curve_fit(linear_model, x, y)

    return {
        "a_estimated": params[0],
        "b_estimated": params[1],
    }


def main() -> None:
    print_string("Curve Fitting")

    results = curve_fitting()

    for k, v in results.items():
        print(k, "=", v)


if __name__ == "__main__":
    main()
