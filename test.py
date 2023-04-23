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
    
    for i in range(tests):
        color: tuple[int, int, int] = get_random_color(test_rng)
        # asserts entropy is used correctly from input
        assert (
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
            exp_rng.randint(0, 255),
        ) == color, "Entropy source is not from input"

if __name__ == "__main__":
    test_colors()