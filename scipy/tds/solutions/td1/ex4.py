import numpy as np
from scipy import fft


def print_string(s: str = '', sep: str = "=") -> None:
    print('\n' + sep * 31 + " " + s + " " + sep * 31 + '\n')


def array_infos(arr: np.ndarray) -> None:
    print("Array Infos ")
    print("Array: \n", arr[:10])
    print("Shape:", arr.shape)
    print()


def fft_signal() -> dict[str, np.ndarray]:
    """
    Compute FFT of a sinusoidal signal.

    Returns
    -------
    dict[str, np.ndarray]
    """
    fs = 100  # sampling frequency
    t = np.linspace(0, 1, fs)
    f = 5

    signal = np.sin(2 * np.pi * f * t)

    fft_values = fft.fft(signal)
    freqs = fft.fftfreq(len(signal), d=1/fs)

    return {
        "signal": signal,
        "fft": np.abs(fft_values),
        "frequencies": freqs,
    }


def main() -> None:
    print_string("FFT")

    for k, v in fft_signal().items():
        print(k)
        array_infos(v)


if __name__ == "__main__":
    main()
