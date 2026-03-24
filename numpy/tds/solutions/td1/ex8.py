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

def array_infos(arr : np.ndarray | float) -> None:
    """
    Print information about a given NumPy array.

    Args:
        arr (np.ndarray): The input array to analyze.

    Returns:
        None
    """
    print("Array Infos ")
    if isinstance(arr, np.ndarray):
        print("Array: \n", arr)
        print("Dimensions:", arr.ndim)
        print("Shape:", arr.shape)
        print("Size:", arr.size)
        print("Dtype:", arr.dtype)
    else:
        print("Value:", arr)
    print()


def weather_analysis() -> dict[str, np.ndarray | float]:
    """
    Analyze simulated weather data.

    Returns:
        dict: Weather statistics
    """
    temperatures: np.ndarray = np.random.uniform(-5, 35, (30, 5))

    heat_mask: np.ndarray = temperatures > 30

    return {
        "city_means": np.mean(temperatures, axis=0),
        "hottest_days": np.argmax(temperatures, axis=0),
        "global_mean": float(np.mean(temperatures)),
        "heat_days_per_city": np.sum(heat_mask, axis=0),
    }

def main() -> None:
    """
    Main function to execute the weather analysis.

    Returns:
        None
    """
    print_string("Weather Analysis")

    results : dict[str, np.ndarray | float] = weather_analysis()

    print("City Means:")
    array_infos(results["city_means"])

    print("Hottest Days:")
    array_infos(results["hottest_days"])

    print(f"Global Mean Temperature: {results['global_mean']} \n")

    print("Heat Days Per City:")
    array_infos(results["heat_days_per_city"])

if __name__ == "__main__":
    main()
