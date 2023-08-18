from abc import ABC
from abc import abstractmethod
from functools import wraps


class Percentage(ABC):
    def __init__(self, minimum=0, maximum=100):
        self.minimum = minimum
        self.maximum = maximum
        self.value = MinMaxLevelNumber(self.minimum, self.maximum)
        self.captions = []

    def add_caption(self, caption):
        assert issubclass(caption, PercentageCaption), ValueError
        cap = caption()
        self.captions.append(cap.register(self))

    def add_value(self, value):
        self.value.set_value(self.value.get_level() + value)

    def clear(self):
        self.value.set_value(self.minimum)
        for cap in self.captions:
            cap.register(self)

    @abstractmethod
    def update(self):
        raise NotImplementedError

    def get_value(self):
        return self.value.get_level()

    def get_minimum(self):
        return self.minimum

    def get_maximum(self):
        return self.maximum


class PercentageCaption(ABC):
    @abstractmethod
    def register(self, percentage: Percentage) -> 'PercentageCaption':
        raise NotImplementedError

    @abstractmethod
    def process(self) -> str:
        raise NotImplementedError


def min_max_setting(func):
    @wraps(func)
    def inner(*args):
        self, min, max = args
        assert min < max, ValueError
        self.__dict__["min"] = min
        self.__dict__["max"] = max
        self.__dict__["level"] = min

    return inner


class MinMaxLevelNumber:
    @min_max_setting
    def __init__(self, min, max):
        ...

    def set_value(self, value):
        self.level = value

    def get_level(self):
        return self.level

    def __setattr__(self, key, value):
        assert self.min <= value <= self.max, ValueError
        self.__dict__[key] = value

    def __repr__(self):
        return f"{self.level}"
