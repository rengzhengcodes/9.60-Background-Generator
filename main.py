"""The image generation algorithm"""

# random library for random background color fixing
from random import Random

# image editing software for generation
from PIL import Image


def get_random_color(rng: Random) -> tuple:
    """Generates a random RGB color tuple

    Attributes:
        rng: The rng source.
    
    Returns:
        A tuple of form (r, g, b)
    """

    return (
            rng.randint(0, 255),
            rng.randint(0, 255),
            rng.randint(0, 255)
        )


def get_canvas_and_brush(
    size: tuple = (256, 256), seed: int = 42
) -> tuple[Image, Random]:
    """
    """

if __name__ == "__main__":
    entropy: Random = Random(42)

    # ensures no 
    print(get_random_color(entropy))