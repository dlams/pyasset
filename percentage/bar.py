# from percentage import Percentage
from enum import Enum
from functools import wraps

from percentage import percentage


class Color(Enum):
    RED = "\x1b[1;31m",
    GREEN = "\x1b[1;32m",
    GRAY = "\x1b[1;37m",
    NONE = "\033[0m",


def cartridge_return(func):
    @wraps(func)
    def returned(*args, **kwargs):
        print("\r", end="")
        result = func(*args, **kwargs)
        return result

    return returned


def color_print(color=Color.NONE):
    def colored(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(color.value[0]) + str(func(*args, **kwargs))
        return wrapper
    return colored


class BarPercentage(percentage.Percentage):
    def __init__(self, mimnum=0, maximum=100):
        super().__init__(mimnum, maximum)
        self.shape = "━"
        self.stage = 50

    @cartridge_return
    def update(self):
        pass_blocks = int(self.value.get_level() / self.maximum * self.stage)
        result = self.get_perfect_bar() if pass_blocks == self.stage else self.get_not_perfect_bar(pass_blocks)
        print(result, end="")
        self.print_captions()

    @color_print(Color.GREEN)
    def get_perfect_bar(self):
        return self.shape * self.stage

    def get_not_perfect_bar(self, pass_blocks):
        return self.get_cleared_bar(pass_blocks) + self.get_not_cleared_bar(pass_blocks)

    @color_print(Color.RED)
    def get_cleared_bar(self, pass_blocks):
        return self.shape * pass_blocks

    @color_print(Color.GRAY)
    def get_not_cleared_bar(self, pass_blocks):
        return self.shape * (self.stage - pass_blocks)

    def print_captions(self):
        print("", end=" ")
        for cap in self.captions:
            print(self.get_caption(cap), end=" ")

    @color_print(Color.NONE)
    def get_caption(self, caption):
        return caption.process()
