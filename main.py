"""The image generation algorithm"""

# random library for random background color fixing
from random import Random
# math calculation library
from math import ceil, floor, log2, pow

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


def generate_blocks_and_offsets(
    size: int, dividers: int = 0
) -> dict[tuple[int, int], tuple[tuple[int, int]]]:
    """
    Attributes:
        size: The size of the image to generate. Assumes exp of 2.
        dividers: Number of block divisions per side.
    Returns:
        A dictionary where the keys are tuples of the top left corners of each
        block and the list the tuples fo the offsets of each side.
    """

    # The number of divisions you can make in a image of size x
    size_exp: int = floor(log2(size))
    # the size of the divisions
    div_size: int = ceil(2 ** (size_exp - dividers))

    # tracks the return value
    ret: dict[tuple[int, int], tuple[tuple[int, int]]] = {}

    # generates the blocks assuming a square
    for row_start in range(0, div_size, size):
        for col_start in range(0, div_size, size):

            # initializes the list
            ret[(row_start, col_start)] = []

            # generates the offsets per block
            for row_off in range(div_size):
                for col_off in range(div_size):

                    ret[(row_start, col_start)].append((row_off, col_off))

            # tuples the offsets
            ret[(row_start, col_start)] = tuple(ret[(row_start, col_start)])

    return ret


def generate_background(
    size: int = 256, seed: int = 42, difficulty: int = 0
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

