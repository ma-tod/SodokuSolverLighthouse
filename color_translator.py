from enum import Enum

class Color(Enum):
    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    YELLOW = [255, 255, 0]
    BLUE = [128, 0, 0]
    PURPLE = [160, 32, 240]
    MAGENTA = [255, 0, 255]
    BROWN = [165, 42, 42]
    CYAN = [0, 255, 255]
    GRAY = [190, 190, 190]


COLOR_TRANSLATOR = {"0": Color.BLACK.value,
                    "1": Color.RED.value,
                    "2": Color.GREEN.value,
                    "3": Color.YELLOW.value,
                    "4": Color.BLUE.value,
                    "5": Color.PURPLE.value,
                    "6": Color.MAGENTA.value,
                    "7": Color.BROWN.value,
                    "8": Color.CYAN.value,
                    "9": Color.GRAY.value,
                    }