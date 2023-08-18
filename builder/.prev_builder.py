from functools import partial


class Builder:
    def __init__(self, cls):
        temp_cls = cls()
        self.main_class = cls
        self.__parameters = {}
        for param in temp_cls.__dict__:
            self.__dict__[param] = partial(self.__add_parameter, param)

    def __add_parameter(self, key, value):
        self.__parameters[key] = value
        return self

    def build(self):
        result = self.main_class()
        result.__dict__.update(self.__parameters)
        return result

    def __str__(self):
        return f"Builder of {self.main_class.__name__}"

    def __repr__(self):
        return f"Builder of {self.main_class.__name__}, {self.__parameters}"
