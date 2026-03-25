import numpy as np
from scipy import fft


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def signal_analysis() -> dict[str, np.ndarray]:
    """
    Analyze composite signal.

    Returns
    -------
    dict[str, np.ndarray]
    """
    fs = 8000
    t = np.linspace(0, 1, fs)

    signal = (
        np.sin(2 * np.pi * 440 * t) +
        0.5 * np.sin(2 * np.pi * 880 * t) +
        0.3 * np.sin(2 * np.pi * 1320 * t)
    )

    noise = np.random.normal(0, 0.2, size=t.shape)
    signal_noisy = signal + noise

    spectrum = fft.fft(signal_noisy)

    return {
        "signal": signal_noisy,
        "spectrum": np.abs(spectrum),
    }


def main() -> None:
    print_string("Signal Analysis")

    results = signal_analysis()

    for k, v in results.items():
        print(k)
        print(v[:10], "\n")


if __name__ == "__main__":
    main()
