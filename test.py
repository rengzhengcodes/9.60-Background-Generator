# ensures all values are >= 255
from main import *

def test_colors(tests: int = 1000):
    """
    Tests the color values of get_color
    """
    # sets the RNG entropy value
    test_rng: Random = Random(42)
    exp_rng: Random = Random(42)

    for i in range(tests):
        color: tuple[int, int, int] = get_random_color(test_rng)
        # asserts entropy is used correctly from input
        assert (
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
        ) == color, "Entropy source is not from input"
        # asserts the colors are less than or equal to 255 and nonnegative and ints
        color_check: tuple[bool] = (
            isinstance(value, int) and (0 <= value <= 255) for value in color
        )
        assert all(color_check), "Colors are not ints in [0, 255]."
    
    test_rng2: Random = Random(34)
    exp_rng2: Random = Random(34)

    for i in range(tests):
        color: tuple[int, int, int] = get_random_color(test_rng2)
        # asserts entropy is used correctly from input
        assert (
            exp_rng2.randint(0, 255),
            exp_rng2.randint(0, 255),
            exp_rng2.randint(0, 255),
        ) == color, "Entropy source is not from input"
        # asserts the colors are less than or equal to 255 and nonnegative and ints
        color_check: tuple[bool] = (
            isinstance(value, int) and (0 <= value <= 255) for value in color
        )
        assert all(color_check), "Colors are not ints in [0, 255]."
    
    for i in range(tests):
        color: tuple[int, int, int] = get_random_color(test_rng)
        # asserts entropy is used correctly from input
        assert (
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
        ) == color, "Entropy source is not from input"
        # asserts the colors are less than or equal to 255 and nonnegative and ints
        color_check: tuple[bool] = (
            isinstance(value, int) and (0 <= value <= 255) for value in color
        )
        assert all(color_check), "Colors are not ints in [0, 255]."

if __name__ == "__main__":
    print("testing colors")
    test_colors()