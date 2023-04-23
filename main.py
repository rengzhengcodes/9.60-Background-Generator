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
    """Creates an Image of the specified size. Returns a Random with the given
    seed.

    Attributes:
        size: The size of the board we're implementing
        seed: The RNG seed.
    Returns:
        A tuple of form (Image, seed)
    """
    return (Image.new("RGB", size), Random(seed))


def generate_background(
    size: tuple = 256, seed: int = 42, difficulty: int = 0
):
    """
    Attributes:
        size: The size of the square
        seed: The seed of the brush
        difficulty: The difficulty of the background
    
    Returns:
        A background of difficulty (2^difficulty differed tiles).
    """
    canvas: Image
    brush: Random
    canvas, brush = get_canvas_and_brush((size, size), seed)

    return canvas

